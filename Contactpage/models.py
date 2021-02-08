from django.db import models


# Create your models here.
class ContactBreadcrumb(models.Model):
	breadcrumb_image = models.ImageField(upload_to='contactpage/images')
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.pk and ContactBreadcrumb.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return 'Bread-crumb background image'

	class Meta:
		verbose_name_plural = 'Breadcrumb'



class ContactForm(models.Model):
	address = models.CharField(max_length=255, blank=True)
	contact_number = models.CharField(max_length=50, blank=True)
	email_address = models.EmailField(max_length=100, blank=True)

	def __str__(self):
		return self.address

	class Meta:
		verbose_name_plural = 'Contact Form'
