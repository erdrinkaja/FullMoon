from django.shortcuts import render
from entities.models.event import Event
from entities.models.moon import Moon
from entities.models.phase import Phase
from entities.models.category import Category
from datetime import datetime


def event(requet):

    moon = Moon.objects.filter(valid_date=datetime.now().date())[0]
    category = Category.objects.all()
    event = Event.objects.all()
    phase_id = moon.phase_id
    phase = Phase.objects.filter(pk=phase_id)[0]
    moon_img_url = phase.image.url


    return render(requet, 'pages/event-discript-page.html', context={'category': category , 'event': event, 'img_url': moon_img_url })
