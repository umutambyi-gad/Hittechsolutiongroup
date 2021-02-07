from django.urls import path
from . import views


app_name = 'blogpage'
urlpatterns = [
    path('', views.blog, name='blog')
]
