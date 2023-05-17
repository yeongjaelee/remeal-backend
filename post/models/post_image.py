from django.db import models


class PostImage(models.Model):
    post = models.ForeignKey('post', models.CASCADE, related_name="images")
    image = models.ImageField(null=True)

    class Meta:
        db_table = 'post_image'
