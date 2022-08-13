
from django.shortcuts import render
from entities.models.phase import Phase
from .page_view import discription, moon

phase_id = moon.phase_id
phase = Phase.objects.filter(pk=phase_id)[0]
moon_img_url = phase.image.url


def event_discription():
    if moon.phase_day == 1:
        return phase.first_description
    if moon.phase_day == 2:
        return phase.second_description
    else:
        return phase.third_description


def event_page(requet):
    img_url = moon_img_url
    event_discript = event_discription()
    moon_discript = discription()

    return render(requet, 'pages/event-discript-page.html', context={'img_url': img_url, 'event_discript': event_discript, 'moon_discript': moon_discript })

