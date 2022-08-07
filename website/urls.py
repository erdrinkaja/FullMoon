"""fullmoon URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from website.views.contact_page import ContactPage
from website.views.event_page import EventPage
from website.views.fortune_teller_page import FortuneTellerPage
from website.views.page_view import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='website-home-page'),
    path('events', EventPage.as_view(), name='website-event-page'),
    path('fortune-teller', FortuneTellerPage.as_view(), name='website-fortune-teller-page'),
    path('contact', ContactPage.as_view(), name='website-contact-page')
]
