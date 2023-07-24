from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy

from blog.forms import PostForm
from blog.models import Comment, Post


class CommentDispMixin:
    template_name = 'blog/comment.html'
    model = Comment
    pk_url_kwarg = 'comment_pk'
    POST = None

    def dispatch(self, request, *args, **kwargs):
        self.POST = get_object_or_404(Post, pk=kwargs['pk'])
        if self.get_object().author != request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class CommentUrlMixin:

    def get_success_url(self):
        return reverse_lazy('blog:post_detail', kwargs={'pk': self.POST.pk})


class CommentValidMixIn:

    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.post = self.POST
        return super().form_valid(form)


class PostUrlMixin:
    template_name = 'blog/create.html'
    model = Post

    def get_success_url(self):
        user = self.request.user
        return reverse_lazy('blog:profile', kwargs={'username': user})


class PostDispatchMixin:

    def dispatch(self, request, *args, **kwargs):
        instance = get_object_or_404(Post, pk=kwargs['pk'])
        if instance.author != request.user:
            return redirect("blog:post_detail", pk=self.kwargs["pk"])
        return super().dispatch(request, *args, **kwargs)


class PostValidMixin:
    form_class = PostForm

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PaginatorMixin:
    paginate_by = 10
