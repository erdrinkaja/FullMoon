
from django.db import models


class Phase(models.Model):
    id = models.IntegerField(primary_key=True, editable=True)
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='phases')
    first_description = models.TextField()
    second_description = models.TextField()
    third_description = models.TextField()

    def __str__(self):
        return self.title
