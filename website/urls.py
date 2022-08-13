
from django.urls import path, include

from website.views.contact_page import ContactPage
from website.views.event_page import event_page
from website.views.event import event
from website.views.fortune_teller_page import FortuneTellerPage
from website.views.page_view import home_page

urlpatterns = [
    path('', home_page, name='website-home-page'),
    path('events/', event_page, name='website-event-page'),
    path('event/', event, name='website-event-discript-page'),
    path('fortune-teller', FortuneTellerPage.as_view(), name='website-fortune-teller-page'),
    path('contact', ContactPage.as_view(), name='website-contact-page')
]
