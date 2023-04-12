from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=255, null=True)
    content = models.TextField(null=True)
    main_image = models.ImageField(null=True)
    date_created = models.DateTimeField(auto_now=True)