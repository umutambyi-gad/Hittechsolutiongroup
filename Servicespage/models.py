from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
class ServicesBreadcrumb(models.Model):
	breadcrumb_image = CloudinaryField('servicepage/images')
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.pk and ServicesBreadcrumb.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return 'Bread-crumb background image'

	class Meta:
		verbose_name_plural = 'Breadcrumb'



class ServicesSection(models.Model):
	heading = models.CharField(max_length=255)
	short_decription = models.CharField(max_length=500)

	def save(self, *args, **kwargs):
		if not self.pk and ServicesSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.heading

	class Meta:
		verbose_name_plural = 'Services section'


class Services(models.Model):
	icon = models.CharField(max_length=100)
	service_title = models.CharField(max_length=100)
	service_description = models.CharField(max_length=500)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.service_title

	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Services'


class KeyFeatureSection(models.Model):
	heading = models.CharField(max_length=255)
	short_decription = models.CharField(max_length=500)

	def save(self, *args, **kwargs):
		if not self.pk and KeyFeatureSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.heading

	class Meta:
		verbose_name_plural = 'Key feature section'


class KeyFeatures(models.Model):
	icon = models.CharField(max_length=100)
	feature_title = models.CharField(max_length=100)
	feature_description = models.CharField(max_length=500)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.feature_title

	class Meta:
		verbose_name = 'Key feature'
		verbose_name_plural = 'Key features'