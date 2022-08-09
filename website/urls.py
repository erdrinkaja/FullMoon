
from django.contrib import admin
from django.urls import path, include

from website.views.contact_page import ContactPage
from website.views.event_page import EventPage
from website.views.fortune_teller_page import FortuneTellerPage
from website.views.page_view import HomePage

urlpatterns = [
    path('', HomePage.as_view(), name='website-home-page'),
    path('events/', EventPage.as_view(), name='website-event-page'),
    path('fortune-teller', FortuneTellerPage.as_view(), name='website-fortune-teller-page'),
    path('contact', ContactPage.as_view(), name='website-contact-page')
]
