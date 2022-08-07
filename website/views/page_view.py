# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = 'pages/home-page.html'
