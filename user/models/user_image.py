from django.db import models

from user.models import User


class UserImage(models.Model):
    user = models.ForeignKey(User, related_name='image', on_delete=models.CASCADE)
    image = models.ImageField(null=True, upload_to='user_image')
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'user_image'
