from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(ServicesBreadcrumb)

class ServicesSectionAdmin(admin.ModelAdmin):
	list_display = ('heading',)

admin.site.register(ServicesSection, ServicesSectionAdmin)

class ServicesAdmin(admin.ModelAdmin):
	list_display = ('service_title', 'added_date')
	list_filter = ('added_date',)

admin.site.register(Services, ServicesAdmin)

class KeyFeatureSectionAdmin(admin.ModelAdmin):
	list_display = ('heading',)

admin.site.register(KeyFeatureSection, KeyFeatureSectionAdmin)

class KeyFeaturesAdmin(admin.ModelAdmin):
	list_display = ('feature_title', 'added_date')
	list_filter = ('added_date',)

admin.site.register(KeyFeatures, KeyFeaturesAdmin)