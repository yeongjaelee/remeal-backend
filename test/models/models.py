from django.db import models

# Create your models here.

class Models(models.Model):
    number = models.IntegerField(null=True)