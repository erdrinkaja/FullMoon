
from django.db import models


class Event(models.Model):
    id = models.IntegerField(primary_key=True)
    title = models.CharField(max_length=255)
    status = models.IntegerField()

    def __str__(self):
        return self.title