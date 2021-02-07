from django.urls import path
from . import views


app_name = 'servicespage'
urlpatterns = [
    path('', views.service, name='services')
]
