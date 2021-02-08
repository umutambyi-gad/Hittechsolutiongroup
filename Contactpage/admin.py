from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(ContactBreadcrumb)

class ContactFormAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('contact_number', 'email_address')
		}),
		('Add address precisely like(street, city, country, region)', {
			'fields': ('address', )
		})
	)
	list_display = ('address', )

admin.site.register(ContactForm, ContactFormAdmin)
