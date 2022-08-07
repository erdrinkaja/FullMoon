# -*- encoding: utf-8 -*-
__author__ = "Aris Mamo"

from django.views.generic import TemplateView


class ContactPage(TemplateView):
    template_name = 'pages/contact-page.html'
