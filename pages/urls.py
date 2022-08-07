from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='home page'),
    path('about/', views.AboutPage.as_view(), name='about page'),
    path('contact/', views.ContactPage.as_view(), name='contact page'),
    path('events/', views.Event.as_view(), name='event page'),

]
