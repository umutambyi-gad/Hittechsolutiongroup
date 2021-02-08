from django.shortcuts import render
from Memberspage.views import ajax_operation
from .models import *
from Contactpage.models import *


# Create your views here.
def service(request):
	contacts = ContactForm.objects.all()
	address = ''
	number = ''
	email = ''
	for contact in contacts:
		address = contact.address
		number = contact.contact_number
		email = contact.email_address

	context = {
		'services_section': ServicesSection.objects.first(),
		'services': Services.objects.all(),
		'feature_section': KeyFeatureSection.objects.first(),
		'key_features': KeyFeatures.objects.all(),
		'breadcrumb': ServicesBreadcrumb.objects.first(),
		'address': address,
		'number': number,
		'email': email
	}


	if request.is_ajax():
		return ajax_operation(request)
	return render(request, 'services.html', context)