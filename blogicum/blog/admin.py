from django.contrib import admin

from .models import Category, Location, Post, Comment


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'pub_date',
        'author',
        'location',
        'category',
        'is_published',
        'created_at',
    )
    list_editable = (
        'is_published',
        'author',
        'location',
        'category',
        'pub_date'
    )
    search_fields = (
        'title',
        'text',
        'author',
        'location',
        'category'
    )
    list_filter = (
        'author',
        'location',
        'category'
    )


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
    )


class LocationAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'name',
    )


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'created_at',
        'author',
        'post',
    )


admin.site.register(Category, CategoryAdmin)
admin.site.register(Location, LocationAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment, CommentAdmin)
