from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import *
from Memberspage.views import ajax_operation


# Create your views here.
def contact(request):
	if request.is_ajax():
		return ajax_operation(request)
		
	if request.method == 'POST':
		if not request.user.is_authenticated:
			sender_name = request.POST['sender_name']
		else:
			sender_name = request.user.get_full_name()

		subject = request.POST['subject']
		sender_email = request.POST['sender_email']
		message = request.POST['message']

		send_mail(subject, # subject
				  f'{sender_name} sends {message}', # message
				  sender_email, # from_email
				  ['umutambyig@gmail.com'])
		return redirect('/contact/')

	contacts = ContactForm.objects.all()

	address = ''
	number = ''
	email = ''
	for contact in contacts:
		address = contact.address
		number = contact.contact_number
		email = contact.email_address

	context = {
		'breadcrumb': ContactBreadcrumb.objects.first(),
		'address': address,
		'number': number,
		'email': email
	}
	
	return render(request, 'contact.html', context)
