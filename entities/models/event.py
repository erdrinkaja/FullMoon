
from django.db import models
from django.db.models import SET_NULL

from entities.models.category import Category


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    status = models.IntegerField()
    category = models.ForeignKey(Category, null=True, blank=True, on_delete=SET_NULL, related_name='events')

    def __str__(self):
        return self.title