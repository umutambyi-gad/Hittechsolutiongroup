from django.urls import path
from . import views


app_name = 'blogpage'
urlspatterns = [
    path('', views.blog, name='blog')
]
