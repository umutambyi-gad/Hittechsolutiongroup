from django.urls import path
from . import views


app_name = 'contactpage'
urlpatterns = [
	path('', views.contact, name='contact')
]
