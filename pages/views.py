from django.shortcuts import render
from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = 'pages/home_page.html'


class AboutPage(TemplateView):
    template_name = 'pages/about_page.html'


class ContactPage(TemplateView):
    template_name = 'pages/contact_page.html'
