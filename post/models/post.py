from django.db import models

from post.models.tag import Tag
from user.models import User


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField(Tag, null=True, related_name='posts')
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    date_created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'post'