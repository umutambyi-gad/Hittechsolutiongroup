from django.urls import path
from . import views


appname = 'aboutpage'
urlpatterns = [
    path('', views.about, name='about')
]
