# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.views.generic import TemplateView


class FortuneTellerPage(TemplateView):
    template_name = 'pages/fortune-teller-page.html'
