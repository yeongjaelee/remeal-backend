from django.db import models

class Tag(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return '{}'.format(self.name)