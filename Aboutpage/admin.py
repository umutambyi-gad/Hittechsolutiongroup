from django.contrib import admin
from .models import *


# Register your models here.
admin.site.register(AboutBreadcrumb)

class HitTechSolutionGroupHistoryAdmin(admin.ModelAdmin):
	message = 'Section for adding images from 1 to 5 so if you want add image click on show then upload them'
	fieldsets = (
		(None, {
			'fields': ('title', 'paragraph')
			}),
		(message, {
			'classes': (
				'collapse'
				, ),
			'fields': (
				'image_1',
				'image_2',
				'image_3',
				'image_4',
				'image_5'
				)
			})
	)

	list_display = ('title', 'added_date')

admin.site.register(HitTechSolutionGroupHistory, HitTechSolutionGroupHistoryAdmin)

class StatisticSectionAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': ('title', 'paragraraph')
			}),
		('Background image section', {
			'fields': ('background_image', )
			})
	)
	list_display = ('title', )

admin.site.register(StatisticSection, StatisticSectionAdmin)

class StatisticsAdmin(admin.ModelAdmin):
	list_display = ('label', 'added_date')

admin.site.register(Statistics, StatisticsAdmin)