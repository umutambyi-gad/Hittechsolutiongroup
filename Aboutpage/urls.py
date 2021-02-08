from django.urls import path
from . import views


app_name = 'aboutpage'

urlpatterns = [
	path('', views.about, name='about')
]