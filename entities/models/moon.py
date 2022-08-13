
from django.db import models
from django.db.models import CASCADE
from entities.models.phase import Phase


class Moon(models.Model):
    valid_date = models.DateField()
    status = models.IntegerField()
    phase = models.ForeignKey(Phase, on_delete=CASCADE)
    phase_day = models.IntegerField()

    def __str__(self):
        return f"{self.valid_date } - {str(self.status)} - {self.phase.title}"