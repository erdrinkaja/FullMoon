
from django.db import models
from django.db.models import CASCADE

from entities.models.base_entity import BaseEntity
from entities.models.phase import Phase


class Moon(BaseEntity):

    valid_date = models.DateField()
    status = models.IntegerField()
    phase_day = models.IntegerField()
    phase = models.ForeignKey(Phase, on_delete=CASCADE)

    def __str__(self):
        return f"{self.valid_date } - {str(self.status)} - {self.phase.title}"


