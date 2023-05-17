from django.db import models

from post.models import Post
from user.models import User


class LikeOnPost(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    is_like = models.BooleanField(default=False)

    class Meta:
        db_table = 'like_on_post'
