from django.shortcuts import render, redirect
from .models import *
from Contactpage.models import *
from Blogpage.models import Blogs
from calendar import month_abbr
from django.conf import settings
from Memberspage.views import ajax_operation
from django.http import JsonResponse


# Create your views here.
def home(request):
	if request.is_ajax():
		message = request.POST.get('message', None)
		if message not in ('', None):
			testimony, created = TestimonyAuthor.objects.update_or_create(
				user=request.user,
				defaults={
					'testimony': message
				}
			)
			testimony.save()
			
			return JsonResponse({
				'isUpdate': TestimonyAuthor.objects.filter(user=request.user.id).exists(),
				'user_id': request.user.id,
				'message': message,
			}, status=200);

		return ajax_operation(request)
	context = {}
	
	if request.method == 'POST':

		message = request.POST['message']
		testimony, created = TestimonyAuthor.objects.update_or_create(
			user=request.user,
			defaults={
				'testimony': message
			}
		)
		testimony.save()
		return redirect('/')

	home_background = HomeBackground.objects.all()
	home_services = HomeDisplayServices.objects.all()
	testimonial_section = TestimonialSection.objects.first()
	testimonial_adding_section = TestimonyAddingSection.objects.first()
	testimonies =  TestimonyAuthor.objects.all()
	offer_section = WhatWeOfferSection.objects.first()
	we_offer = WhatWeOffer.objects.all()
	galleries = FooterGallery.objects.all()
	recent_blogs = Blogs.recent_blogs()

	contacts = ContactForm.objects.all()

	address = ''
	number = ''
	email = ''
	for contact in contacts:
		address = contact.address
		number = contact.contact_number
		email = contact.email_address

	suffer = ''
	for i in recent_blogs:
		suffer = month_abbr[i.blog_added_date.month]
	
	context = {
				'backgrounds': home_background,
				'services': home_services,
				'testimonial_section': testimonial_section,
				'testimonies': testimonies,
				'testimonial_adding': testimonial_adding_section,
				'offer_section': offer_section,
				'we_offer': we_offer,
				'galleries':  galleries,
				'recent_blogs': recent_blogs,
				'suffer': suffer,
				'address': address,
				'number': number,
				'email': email
			}

	return render(request, 'index.html', context)
