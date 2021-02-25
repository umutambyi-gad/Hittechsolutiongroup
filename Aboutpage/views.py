from django.shortcuts import render
from .models import *
from Contactpage.models import *
from Homepage.models import *
from Memberspage.views import ajax_operation


# Create your views here.
def about(request):
	if request.is_ajax():
		return ajax_operation(request)
	galleries = FooterGallery.objects.all()
	history = HitTechSolutionGroupHistory.objects.all()
	statistics_section = StatisticSection.objects.first()
	statistics = Statistics.objects.all()

	contacts = ContactForm.objects.all()
	address = ''
	number = ''
	email = ''
	for contact in contacts:
		address = contact.address
		number = contact.contact_number
		email = contact.email_address

	title = ''
	paragraph = ''
	for column in history:
		title = column.title
		paragraph = column.paragraph

	content_paragraph = formatting(paragraph)

	context = {
	'contents_head': title,
	'contents': content_paragraph,
	'statistics': statistics,
	'statistics_section': statistics_section,
	'galleries' : galleries,
	'breadcrumb': AboutBreadcrumb.objects.first(),
	'address': address,
	'number': number,
	'email': email
	}
	return render(request, 'about.html', context)
