

from django.views.generic import TemplateView


class FortuneTellerPage(TemplateView):
    template_name = 'pages/fortune-teller-page.html'
