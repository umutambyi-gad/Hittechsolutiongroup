from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(BlogBreadcrumb)

class TagsAdmin(admin.ModelAdmin):
	list_display = ('tag', 'created')

admin.site.register(Tags, TagsAdmin)

class CategoriesAdmin(admin.ModelAdmin):
	list_display = ('category', 'created')

admin.site.register(Categories, CategoriesAdmin)

class BlogsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'blog_title',
				'blog_short_description',
				'blog_content'
				)
			}),
		('Section for background image of an article or thumbnail', {
			'fields': (
				'blog_thumbnail',
				)
			}),
		('Why you wrote this blog? tell something about why you wrote this', {
			'fields': (
				'blog_author_description'
			,)
		}),
		('Section for including images in blog', {
			'classes': (
				'collapse'
				),
			'fields': (
				'blog_image_1',
				'blog_image_2',
				'blog_image_3',
				'blog_image_4',
				'blog_image_5'
				)
			}),
		('Blog category adding section', {
			'fields': (
				'blog_category',
				)
		}),
		('Blog tags adding section', {
			'fields': (
				'blog_tag',
				)
			})
	)
	list_filter = ('blog_added_date',)
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

	list_display = ('blog_title', 'user', 'blog_added_date')

admin.site.register(Blogs, BlogsAdmin)

class RootCommentsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'commentor_message',
			),
		}),
	)
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	list_display = ('user', 'added_date')

admin.site.register(RootComments, RootCommentsAdmin)

class ReplyCommentsAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'commentor_message',
			),
		}),
	)
	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)


	list_display = ('user', 'added_date')

admin.site.register(ReplyComments, ReplyCommentsAdmin)

