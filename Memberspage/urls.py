from django.urls import path
from . import views

app_name = 'memberspage'
urlpatterns = [
    path('', views.team, name='team')
]
