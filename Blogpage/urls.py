from django.urls import path
from .views import (blog, blog_single)

app_name = 'blogpage'

urlpatterns = [
	path('', blog, name='blog'),
	path('<int:blog_id>/<slug:blog_title_slug>/', blog_single, name='blog-single'),
]
