from django.contrib import admin

from entities.models.event import Event
from entities.models.moon import Moon
from entities.models.phase import Phase

admin.site.register(Event)
admin.site.register(Moon)
admin.site.register(Phase)
