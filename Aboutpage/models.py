from django.db import models
from cloudinary import CloudinaryField


# Create your models here.
class AboutBreadcrumb(models.Model):
	breadcrumb_image = CloudinaryField('aboutpage/images')
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.pk and AboutBreadcrumb.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return 'Bread-crumb background image'

	class Meta:
		verbose_name_plural = 'Breadcrumb'

class HitTechSolutionGroupHistory(models.Model):
	title = models.CharField(max_length=500)
	paragraph = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	image_1 = CloudinaryField('aboutpage/images'null=True, blank=True)
	image_2 = CloudinaryField('aboutpage/images'null=True, blank=True)
	image_3 = CloudinaryField('aboutpage/images'null=True, blank=True)
	image_4 = CloudinaryField('aboutpage/images'null=True, blank=True)
	image_5 = CloudinaryField('aboutpage/images'null=True, blank=True)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Hit Tech Solution Group History'




class StatisticSection(models.Model):
	title = models.CharField(max_length=500)
	paragraraph = models.TextField()
	background_image = CloudinaryField('aboutpage/images'null=True, blank=True)

	def save(self, *args, **kwargs):
		if not self.pk and StatisticSection.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name_plural = 'Statistic Section'

class Statistics(models.Model):
	number = models.IntegerField()
	label = models.CharField(max_length=200)
	added_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.label

	class Meta:
		ordering = ['label']
		verbose_name_plural = 'Statistics'

