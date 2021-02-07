from django.urls import path
from . import views

app_name = 'memberspage'
urls = [
    path('', views.team, name='team')
]
