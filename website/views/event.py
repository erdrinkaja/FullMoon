from django.shortcuts import render
from entities.models.event import Event
from entities.models.moon import Moon
from entities.models.phase import Phase
from entities.models.category import Category
from datetime import datetime


def event(requet):

    moon = Moon.objects.filter(valid_date=datetime.now().date())[0]
    status = moon.status
    category = Category.objects.all()
    event = Event.objects.all()
    event_st = 1
    phase_id = moon.phase_id
    phase = Phase.objects.filter(pk=phase_id)[0]
    moon_img_url = phase.image.url

    def disc_event():
        if status == 3:
            return 'Be careful, Today is "RED MOON"! Do not take any decision!'
        if status == event_st:
            return "Today is the perfect time tu take this decision!"
        else:
            return "Today is not a good day to take this decision!"

    discript = disc_event()
    return render(requet, 'pages/event-discript-page.html', context={'discription': discript,'category': category , 'event': event, 'img_url': moon_img_url })
