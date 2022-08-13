
from django.db import models


class Category(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    photo = models.ImageField(default=None)

    def __str__(self):
        return self.title
