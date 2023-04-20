
from django.contrib import admin

from post.models import Post, PostImage


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content')

@admin.register(PostImage)
class PostImageAdmin(admin.ModelAdmin):
    pass