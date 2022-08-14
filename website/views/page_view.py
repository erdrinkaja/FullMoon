import random

from django.db.models import Q
from django.shortcuts import render

from entities.models.event import Event
from entities.models.phase import Phase
from entities.models.moon import Moon
from datetime import datetime


def home_page(request):
    moon = Moon.objects.filter(valid_date=datetime.now().date())[0]
    phase_id = moon.phase_id
    st = moon.status
    phase = Phase.objects.filter(pk=phase_id)[0]
    moon_img_url = phase.image.url
    title = phase.title
    event = Event.objects.filter(status=st)
    evn_in_favor = random.choice(event)
    even = Event.objects.filter(~Q(status=st))
    evn_in_disfavor = random.choice(even)

    if moon.phase_day == 1:
        description = phase.first_description
    if moon.phase_day == 2:
        description = phase.second_description
    else:
        description = phase.third_description

    return render(request, 'pages/home-page.html', context={'img_url': moon_img_url, 'description': description, 'title': title, 'ev_in_favor': evn_in_favor, 'ev_in_disfavor': evn_in_disfavor })
