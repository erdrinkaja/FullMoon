

from django.db import models

from entities.models.base_entity import BaseEntity


class Event(BaseEntity):
    title = models.CharField(max_length=255)
    status = models.IntegerField()

    def __str__(self):
        return self.title