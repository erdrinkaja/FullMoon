from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = 'pages/home_page.html'


class FortuneTeller(TemplateView):
    template_name = 'pages/fortune_teller.html'


class ContactPage(TemplateView):
    template_name = 'pages/contact_page.html'


class Event(TemplateView):
    template_name = 'pages/events.html'
