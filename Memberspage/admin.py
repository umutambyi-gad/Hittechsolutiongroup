from django.contrib import admin
from .models import *



# Register your models here.
admin.site.register(MemberBreadcrumb)

admin.site.register(StaffMembersSection)

class MembersAdmin(admin.ModelAdmin):
	fieldsets = (
		(None, {
			'fields': (
				'member_position',
				)
			}),
		('location of member', {
			'fields': (
				'member_country',
				'member_city'
			)
		}),
		('Section for uploading your image Note: upload you own image', {
			'fields': (
				'member_image'
				,)
			}
		),
		('Section for writting something to describe you', {
			'fields': (
				'about_member'
				,)
			}
		),
	)

	def save_model(self, request, obj, form, change):
		obj.user = request.user
		super().save_model(request, obj, form, change)

admin.site.register(Members, MembersAdmin)

class SocialMediaForStaffUsersAdmin(admin.ModelAdmin):
	message = """Add only usernames remember to put slash or underscore if there
	is and if you don't have an account skip the input or create an account first"""
	fieldsets = (
		(message, {
			'fields': (
				'twitter_username',
				'instagram_username',
				'facebook_username',
				'github_username',
				'linkedin_username',
				'stack_overflow_user_id',
				'dribble_username',
				'phone_number'
			)
		}),
	)
	def save_model(self, request, obj, form, change):
		obj.member = request.user.members.pk
		super().save_model(request, obj, form, change)

admin.site.register(SocialMediaForStaffUsers, SocialMediaForStaffUsersAdmin)
