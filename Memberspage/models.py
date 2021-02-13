from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


# Create your models here.
class MemberBreadcrumb(models.Model):
	breadcrumb_image = CloudinaryField('memberspage/images')
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.pk and MemberBreadcrumb.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return 'Bread-crumb background image'

	class Meta:
		verbose_name_plural = 'Breadcrumb'



class StaffMembersSection(models.Model):
	section_heading = models.CharField(max_length=50)
	section_paragraph_description = models.TextField()

	def save(self, *args, **kwargs):
		if not self.pk and StaffMembersSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.section_heading

	class Meta:
		verbose_name_plural = 'Staff members section'


class Members(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	member_position = models.CharField(max_length=60, blank=True, null=True)
	member_country = models.CharField(max_length=60, blank=True, null=True)
	member_city = models.CharField(max_length=60, blank=True, null=True)
	member_image = CloudinaryField('memberspage/images', blank=True, null=True)
	about_member = models.TextField(blank=True, null=True)

	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Members'


class SocialMediaForStaffUsers(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
	member = models.OneToOneField(Members, on_delete=models.CASCADE)
	twitter_username = models.CharField(max_length=100, null=True, blank=True)
	instagram_username = models.CharField(max_length=100, null=True, blank=True)
	facebook_username = models.CharField(max_length=100, null=True, blank=True)
	github_username = models.CharField(max_length=100, null=True, blank=True)
	linkedin_username = models.CharField(max_length=100, null=True, blank=True)
	dribble_username = models.CharField(max_length=100, null=True, blank=True)
	stack_overflow_user_id = models.CharField(max_length=100, null=True, blank=True)
	phone_number = models.CharField(max_length=100, null=True, blank=True)

	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Social media for staff users'

