from django.contrib.auth import get_user_model
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (
    CreateView, DeleteView, DetailView, ListView, UpdateView
)

from core.querys import post_query_set, full_query_set
from .forms import PostForm, ProfileForm, CommentForm
from .models import Post, Category, Comment
from core.mixins import (
    PaginatorMixin, PostValidMixin, PostUrlMixin,
    PostDispatchMixin, CommentUrlMixin, CommentValidMixIn, CommentDispMixin
)

User = get_user_model()


class IndexListView(PaginatorMixin, ListView):
    model = Post
    template_name = 'blog/index.html'
    queryset = post_query_set()


class CategoryListView(PaginatorMixin, ListView):
    template_name = 'blog/category.html'
    SLUG = None

    def get_queryset(self):
        self.SLUG = self.kwargs['slug']
        return post_query_set().filter(category__slug=self.SLUG)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = get_object_or_404(
            Category, slug=self.SLUG, is_published=True
        )
        return context


class PostDetailView(DetailView):
    template_name = 'blog/detail.html'
    model = Post
    POST = None

    def get_queryset(self):
        self.POST = get_object_or_404(Post, pk=self.kwargs["pk"])
        if self.POST.author != self.request.user:
            return post_query_set().filter(pk=self.kwargs["pk"])
        return full_query_set().filter(pk=self.kwargs["pk"])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = CommentForm()
        context['comments'] = self.object.comments.all().select_related(
            "author"
        )
        return context


class PostCreateView(
    LoginRequiredMixin,
    PostValidMixin,
    PostUrlMixin,
    CreateView
):

    pass


class PostUpdateView(
    LoginRequiredMixin,
    PostValidMixin,
    PostDispatchMixin,
    PostUrlMixin,
    UpdateView
):

    pass


class PostDeleteView(
    LoginRequiredMixin,
    PostDispatchMixin,
    PostUrlMixin,
    DeleteView
):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PostForm(instance=self.object)
        return context


class CommentCreateView(
    LoginRequiredMixin,
    CommentUrlMixin,
    CommentValidMixIn,
    CreateView
):
    template_name = 'blog/comment.html'
    model = Comment
    form_class = CommentForm
    POST = None

    def dispatch(self, request, *args, **kwargs):
        self.POST = get_object_or_404(Post, pk=kwargs['pk'])
        return super().dispatch(request, *args, **kwargs)


class CommentUpdateView(
    LoginRequiredMixin,
    CommentValidMixIn,
    CommentUrlMixin,
    CommentDispMixin,
    UpdateView
):
    form_class = CommentForm

    pass


class CommentDeleteView(
    LoginRequiredMixin,
    CommentDispMixin,
    CommentUrlMixin,
    DeleteView
):

    pass


class ProfileListView(PaginatorMixin, ListView):
    template_name = 'blog/profile.html'
    AUTHOR = None

    def get_queryset(self):
        user = self.kwargs['username']
        self.AUTHOR = get_object_or_404(User, username=user)
        if self.AUTHOR != self.request.user:
            return post_query_set().filter(author__username=user)
        return full_query_set().filter(author__username=user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = self.AUTHOR
        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'blog/user.html'
    model = User
    form_class = ProfileForm

    def get_object(self, queryset=None):
        return self.request.user

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('blog:profile', kwargs={'username': user})
