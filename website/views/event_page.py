from django.shortcuts import render
from entities.models.phase import Phase
from entities.models.moon import Moon
from datetime import datetime


def event_page(requet):
    moon = Moon.objects.filter(valid_date=datetime.now().date())[0]
    phase_id = moon.phase_id
    phase = Phase.objects.filter(pk=phase_id)[0]
    moon_img_url = phase.image.url
    def discription():
        if moon.phase_day == 1:
            return phase.first_description
        if moon.phase_day == 2:
            return phase.second_description
        else:
            return phase.third_description
    discript = discription()
    return render(requet, 'pages/event-page.html', context={'img_url': moon_img_url, 'discription': discript })
