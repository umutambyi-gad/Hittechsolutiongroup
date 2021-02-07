from django.urls import path
from . import views


appname = 'aboutpage'
urlspatterns = [
    path('', views.about, name='about')
]
