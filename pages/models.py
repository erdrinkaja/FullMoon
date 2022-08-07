from django.db import models


class Moon(models.Model):
    data = models.DateTimeField(primary_key=True)
    status = models.IntegerField()
    phase = models.IntegerField()
    day_discription = models.IntegerField()

    class Meta:
        verbose_name_plural = 'moon'


class Events(models.Model):
    event_title = models.CharField(max_length=255)
    event_status = models.IntegerField()

    class Meta:
        verbose_name_plural = 'events'


class MoonPhase(models.Model):
    moon_phase = models.IntegerField(primary_key=True)
    moon_image = models.ImageField(upload_to=None)
    description_1 = models.TextField()
    description_2 = models.TextField()
    description_3 = models.TextField()

    class Meta:
        verbose_name_plural = 'moon phase'



