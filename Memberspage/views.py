from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from .models import *
from Contactpage.models import *
from django.http import JsonResponse
from django.contrib import messages


# Create your views here.
def ajax_operation(request):
	if request.is_ajax():
		# for sign in
		__username = request.POST.get('__username', None)
		__password = request.POST.get('__password', None)
		if __username not in (None, '') and __password not in (None, ''):
			user = auth.authenticate(
				username=__username,
				password=__password
			)
			if user is None:
				return JsonResponse({
					'res': 'invalid credentials'
					}, status=200)
		
		# for sign up
		existance = 'not exists'
		_username = request.POST.get('_username', None)
		_email = request.POST.get('_email', None)

		if _username not in (None, '') or _email not in (None, ''):
			if User.objects.filter(username=_username).exists():
				existance = 'exists'

			elif User.objects.filter(email=_email).exists():
				existance = 'exists'

			return JsonResponse({
				'existance': existance
				},
				status=200
			)

	return JsonResponse({}, status=200)


def team(request):
	if request.is_ajax():
		return ajax_operation(request)
		
	members_section = StaffMembersSection.objects.first()
	members = Members.objects.all()
	contacts = ContactForm.objects.all()
	
	address = ''
	number = ''
	email = ''
	for contact in contacts:
		address = contact.address
		number = contact.contact_number
		email = contact.email_address
	context = {
	'members_section': members_section,
	'members': members,
	'breadcrumb': MemberBreadcrumb.objects.first(),
	'address': address,
	'number': number,
	'email': email
	}
	return render(request, 'team.html', context)


def signup(request):
	if request.method == 'POST':
		first_name = request.POST['firstname']
		last_name = request.POST['lastname']
		username = request.POST['username']
		email = request.POST['email']
		last_name = request.POST['lastname']
		password = request.POST['password']
		confirm_password = request.POST['confirm_password']

		if password == confirm_password:
			if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
				messages.info(request, "May be username or email already exists in our database")
				return redirect(request.META['HTTP_REFERER'])
			else:
				user = User.objects.create_user(
					first_name=first_name,
					last_name=last_name,
					username=username,
					email=email,
					password=password,
					)
				user.save()
				membership = Members.objects.create(
					user=user,
					member_image=''
				)
				membership.save()
				messages.success(request, "Successfully signed up so click on signin button to signin")
				return redirect(request.META['HTTP_REFERER'])
		else:
			messages.info(request, "Your passwords doesn't match")
			return redirect(request.META['HTTP_REFERER'])


	return redirect(request.META['HTTP_REFERER'])

def signin(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']

		user = auth.authenticate(
				username=username,
				password=password
			)
		if user is not None:
			auth.login(request, user)
			messages.success(request, f"Successfully signed in as {request.user.username}")
			return redirect(request.META['HTTP_REFERER'])
		else:
			messages.info(request, "You entered invalid credentials")
			return redirect(request.META['HTTP_REFERER'])
	return redirect(request.META['HTTP_REFERER'])


def signout(request):
	auth.logout(request)
	messages.success(request, "Successfully signed out")
	return redirect(request.META['HTTP_REFERER'])


def updateProfile(request, user_id):
	if request.method == 'POST':
		# user setting
		username = request.POST.get('username', None)
		email = request.POST.get('email', None)
		firstname = request.POST.get('firstname', None)
		lastname = request.POST.get('lastname', None)

		if username is None or username.strip() == '':
			username = request.user.username

		if email is None or email.strip() == '':
			email = request.user.email

		if firstname is None or firstname.strip() == '':
			firstname = request.user.first_name

		if lastname is None or lastname.strip() == '':
			lastname = request.user.last_name


		user, created = User.objects.update_or_create(
			pk=request.user.id,
			defaults={
			'username': username,
			'email': email,
			'first_name': firstname,
			'last_name': lastname,
			}
		)

		# members setting
		membership = hasattr(request.user, 'members')
		member_position = ('', request.user.members.member_position)[membership]
		member_country = ('', request.user.members.member_country)[membership]
		member_city = ('', request.user.members.member_city)[membership]
		about_member = ('', request.user.members.about_member)[membership]
		member_image = ('', request.user.members.member_image)[membership]

		position = request.POST.get('position', None)
		country = request.POST.get('country', None)
		city = request.POST.get('city', None)
		about = request.POST.get('about', None)
		image = request.FILES.get('profile', None)

		if position in ('', None):
			position = member_position

		if country in ('', None):
			country = member_country

		if city in ('', None):
			city = member_city

		if about in ('', None):
			about = about_member

		if image in ('', None):
			image = member_image

		member, created = Members.objects.update_or_create(
			user=User.objects.get(pk=user_id),
			defaults={
				'member_position': position,
				'member_country': country,
				'member_city': city,
				'member_image': image,
				'about_member': about
			}
		)
		member.save()
		messages.success(request, 'Successfully user information updated')
	
	return redirect(request.META['HTTP_REFERER'])

def deleteProfile(request, user_id):
	user = User.objects.get(pk=user_id)
	user.delete()
	request.session.clear()
	messages.success(request, 'User successfully deleted')
	return redirect(request.META['HTTP_REFERER'])
