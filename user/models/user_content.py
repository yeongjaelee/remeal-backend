from django.db import models

from user.models import User


class UserContent(models.Model):
    user = models.ForeignKey(User, related_name='contents', on_delete=models.CASCADE)
    content = models.TextField(null=True)
    image = models.ImageField(null=True, upload_to='user_content')

    class Meta:
        db_table = 'user_content'
