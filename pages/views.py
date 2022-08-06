from django.shortcuts import render
from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name = 'pages/home_page.html'


# def home(request):
#     return render(request, 'pages/home_page.html')
