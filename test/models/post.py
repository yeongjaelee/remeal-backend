from django.db import models

# Create your models here.

class Post(models.Model):
    number = models.IntegerField(null=True)