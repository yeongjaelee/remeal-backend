
from django.contrib import admin

from post.models import Post, PostImage, Tag, Comment, LikeOnPost


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'comment')

@admin.register(LikeOnPost)
class LinkOnPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'post', 'is_like')