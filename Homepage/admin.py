from django.contrib import admin
from .models import *


# Register your models here.
admin.site.site_header = 'Hit tech solution group Rwanda Administration'
admin.site.site_title = admin.site.site_header

class HomeBackgroundAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('background_title', 'background_description_paragraph')
		}),
	('Image section', {
		'fields': ('background_image', )
		})
	)
	list_display = ('background_title', 'added_date')

admin.site.register(HomeBackground, HomeBackgroundAdmin)

class HomeDisplayServicesAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('service_title', 'service_description_paragraph')
		}),
	('Flat icon section', {
		'fields': ('service_flaticon_class', )
		})
	)

	list_display = ('service_title', 'added_date')

admin.site.register(HomeDisplayServices, HomeDisplayServicesAdmin)

class WhatWeOfferSectionAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('section_heading', 'section_description_paragraph')
		}),
	('Image section', {
		'fields': ('section_aside_image', )
		})
	)

	list_display = ('section_heading', )


admin.site.register(WhatWeOfferSection, WhatWeOfferSectionAdmin)

class WhatWeOfferAdmin(admin.ModelAdmin):
	fieldsets = (
	(None, {
		'fields': ('offer_title', 'offer_description')
		}),
	('Flat icon section', {
		'fields': ('offer_flaticon_class', )
		})
	)

	list_display = ('offer_title', 'added_date')

admin.site.register(WhatWeOffer, WhatWeOfferAdmin)

class TestimonyAddingSectionAdmin(admin.ModelAdmin):
	list_display = ('testimony_section_heading', )

admin.site.register(TestimonyAddingSection, TestimonyAddingSectionAdmin)


class TestimonyAuthorAdmin(admin.ModelAdmin):
	fields = ('testimony', )
	list_display = ('user', 'added_date')
	list_filter = ('added_date',)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


admin.site.register(TestimonyAuthor, TestimonyAuthorAdmin)

admin.site.register(TestimonialSection)

class FooterGalleryAdmin(admin.ModelAdmin):
	fieldsets = (
	('Footer gallery Images section', {
		'fields': ('image', )
		}),
	)
	list_display = ('added_date', 'image')

admin.site.register(FooterGallery, FooterGalleryAdmin)
