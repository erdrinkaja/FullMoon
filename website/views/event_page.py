# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.views.generic import TemplateView


class EventPage(TemplateView):
    template_name = 'pages/event-page.html'
