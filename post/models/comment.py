from django.db import models

from post.models import Post
from user.models import User


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    comment = models.CharField(max_length=255, null=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'comment'