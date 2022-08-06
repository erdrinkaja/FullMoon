from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Moon)
admin.site.register(models.MoonPhase)
admin.site.register(models.Events)