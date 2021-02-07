from django.urls import path
from . import views


app_name = 'servicespage'
urlspatterns = [
    path('', views.service, name='services')
]
