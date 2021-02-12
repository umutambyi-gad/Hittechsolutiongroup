from django.db import models
from django.contrib.auth.models import User
from cloudinary import CloudinaryField


# Create your models here.
class HomeBackground(models.Model):
	background_image = CloudinaryField('homepage/images')
	background_title = models.CharField(max_length=100)
	background_description_paragraph = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.background_title

	class Meta:
		verbose_name_plural = 'Home Backgrounds'




class HomeDisplayServices(models.Model):
	service_flaticon_class = models.CharField(max_length=100)
	service_title = models.CharField(max_length=40)
	service_description_paragraph = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if HomeDisplayServices.objects.count() == 4:
			return False
		super().save(*args, **kwargs)

	
	def __str__(self):
		return self.service_title

	class Meta:
		verbose_name_plural = 'Home Display Services'




class WhatWeOfferSection(models.Model):
	section_heading = models.CharField(max_length=30)
	section_description_paragraph = models.TextField()
	section_aside_image = CloudinaryField('homepage/images')

	def save(self, *args, **kwargs):
		if not self.pk and WhatWeOfferSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.section_heading

	class Meta:
		verbose_name_plural = 'What We Offer Section'

class WhatWeOffer(models.Model):
	offer_title = models.CharField(max_length=50)
	offer_flaticon_class = models.CharField(max_length=20)
	offer_description = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.offer_title

	class Meta:
		verbose_name_plural = 'What We Offer'




class TestimonyAddingSection(models.Model):
	testimony_section_heading = models.CharField(max_length=100)
	testimonial_background = CloudinaryField('homepage/images')
	testimony_section_description_paragraph = models.TextField()
	
	def save(self, *args, **kwargs):
		if not self.pk and TestimonyAddingSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.testimony_section_heading

	class Meta:
		verbose_name_plural = 'Testimony Adding Section'


class TestimonyAuthor(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	testimony = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Testimony Authors'




class TestimonialSection(models.Model):
	testimonial_heading = models.CharField(max_length=100)
	testimonial_description_paragraph = models.TextField()

	def save(self, *args, **kwargs):
		if not self.pk and TestimonialSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.testimonial_heading

	class Meta:
		verbose_name_plural = 'Testimonial Section'



class FooterGallery(models.Model):
	image = CloudinaryField('homepage/images')
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if FooterGallery.objects.count() == 4:
			return False
		super().save(*args, **kwargs)

	def __str__(self):
		return f"added {str(self.image).split('/')[-1]} image"

	class Meta:
		verbose_name_plural = 'Footer Gallery'
