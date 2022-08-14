
from django.urls import path, include

from website.views.contact_page import ContactPage
from website.views.event_detail import event_detail, event_detail_for_date
from website.views.event import event
from website.views.fortune_teller_page import FortuneTellerPage
from website.views.page_view import home_page

urlpatterns = [
    path('', home_page, name='website-home-page'),
    path('event/<int:id>', event_detail, name='website-event-detail-page'),
    path('event-filter/<int:id>', event_detail_for_date, name='website-event-filter-page'),
    path('event/', event, name='website-event-discript-page'),
    path('fortune-teller', FortuneTellerPage.as_view(), name='website-fortune-teller-page'),
    path('contact', ContactPage.as_view(), name='website-contact-page')
]
