from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home page'),
    path('fortune-teller/', views.FortuneTeller.as_view(), name='fortune teller'),
    path('contact/', views.ContactPage.as_view(), name='contact page'),
    path('events/', views.Event.as_view(), name='event page'),

]
