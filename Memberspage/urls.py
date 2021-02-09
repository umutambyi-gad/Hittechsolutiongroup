from django.urls import path
from . import views


app_name = 'memberspage'

urlpatterns = [
	path('', views.team, name='team'),
	path('sign-up', views.signup, name='sign-up'),
	path('sign-in', views.signin, name='sign-in'),
	path('sign-out', views.signout, name='sign-out'),
	path('<int:user_id>/update-profile', views.updateProfile, name='update-profile'),
	path('<int:user_id>/delete-profile', views.deleteProfile, name='delete-profile'),
]
