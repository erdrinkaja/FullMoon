from django.shortcuts import render

from entities.models.event import Event
from entities.models.phase import Phase
from entities.models.moon import Moon
from datetime import datetime


def event_detail(request, id):

    moon = Moon.objects.filter(valid_date=datetime.now().date())[0]
    phase_id = moon.phase_id
    status_id = moon.status
    phase = Phase.objects.filter(pk=phase_id)[0]
    event = Event.objects.filter(pk=id)[0]
    moon_img_url = phase.image.url

    suggestion = None
    if status_id == 3:
        suggestion = "Careful!!!, Today it is not suggested to make any importand decision because it is a blood moon"
    if status_id == event.status:
        suggestion = "Today, the position of the moon is in your favor. \n If you would like to consider a different date, click the above button."
    else:
        suggestion = "Today, the position of the moon is not in your favor"


    return render(request, 'pages/event-page-detail.html', context={'phase': phase, 'img_url': moon_img_url, 'event': event, 'suggestion': suggestion})


def event_detail_for_date(request, id):
    check_date = request.POST.get('checkDate', None)
    moon = Moon.objects.filter(valid_date=check_date)[0]
    phase_id = moon.phase_id
    status_id = moon.status
    phase = Phase.objects.filter(pk=phase_id)[0]
    event = Event.objects.filter(pk=id)[0]
    moon_img_url = phase.image.url

    suggestion = None
    if status_id == 3:
        suggestion = "Careful!!!, This it is not suggested to make any importand decision because it is a blood moon"
    if status_id == event.status:
        suggestion = "This day, the position of the moon is in your favor. \n If you would like to consider a different date, click the above button."
    else:
        suggestion = "This day, the position of the moon is not in your favor. \n If you would like to consider a different date, click the above button."

    return render(request, 'pages/event-page-detail.html',
                  context={'phase': phase ,'img_url': moon_img_url, 'event': event, 'suggestion': suggestion})