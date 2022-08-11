from django.shortcuts import render
from entities.models.phase import Phase


def home_page(requet):
    phases = Phase.objects.all()
    return render(requet, 'pages/home-page.html', context={'phases': phases})
