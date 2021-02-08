from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

"""
user = User.objects.filter(username='Anonymous')
user_id = [i.id for i in user][0] if user.count() > 0 else 1
Anonymous_user_id = user_id
"""
# Create your models here.
class BlogBreadcrumb(models.Model):
	breadcrumb_image = models.ImageField(upload_to='blogpage/images', default='')
	added_date = models.DateTimeField(auto_now_add=True)

	def save(self, *args, **kwargs):
		if not self.pk and BlogBreadcrumb.objects.exists():
			return False
		return super().save(*args, **kwargs)

	def __str__(self):
		return 'Bread-crumb background image'

	class Meta:
		verbose_name_plural = 'Breadcrumb'


class Tags(models.Model):
	tag = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.tag

	class Meta:
		verbose_name_plural = 'Tags'




class Categories(models.Model):
	category = models.CharField(max_length=150)
	created = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.category

	class Meta:
		verbose_name_plural = 'Categories'



class Blogs(models.Model):
	user = models.OneToOneField(User, on_delete=models.SET(1)) # Anonymous_user_id
	blog_title = models.CharField(max_length=300)
	blog_short_description = models.TextField()
	blog_content = models.TextField()
	blog_thumbnail = models.ImageField(upload_to='blogpage/images')
	blog_category = models.ForeignKey(Categories, on_delete=models.CASCADE)
	blog_tag = models.ManyToManyField(Tags)
	blog_author_description = models.TextField()
	blog_added_date = models.DateTimeField(auto_now_add=True)
	blog_image_1 = models.ImageField(upload_to='blogpage/images', null=True, blank=True)
	blog_image_2 = models.ImageField(upload_to='blogpage/images', null=True, blank=True)
	blog_image_3 = models.ImageField(upload_to='blogpage/images', null=True, blank=True)
	blog_image_4 = models.ImageField(upload_to='blogpage/images', null=True, blank=True)
	blog_image_5 = models.ImageField(upload_to='blogpage/images', null=True, blank=True)

	def slug(self):
		return slugify(self.blog_title)

	@classmethod
	def recent_blogs(cls):
		recents = cls.objects.order_by('-blog_added_date')
		return recents[:3]

	def __str__(self):
		return self.blog_title

	class Meta:
		verbose_name_plural = 'Blogs'


class RootComments(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET(1)) # Anonymous_user_id
	blog = models.ForeignKey(Blogs, on_delete=models.CASCADE)
	commentor_message = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	@classmethod
	def deleteRootComment(cls, comment_id):
		cls.objects.get(pk=comment_id).delete()

	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Root Comments'


class ReplyComments(models.Model):
	user = models.ForeignKey(User, on_delete=models.SET(1)) # Anonymous_user_id
	root_comment = models.ForeignKey(RootComments, on_delete=models.CASCADE)
	commentor_message = models.TextField()
	added_date = models.DateTimeField(auto_now_add=True)

	@classmethod
	def deleteReplyComment(cls, comment_id):
		cls.objects.get(pk=comment_id).delete()
	
	def __str__(self):
		return self.user.get_full_name()

	class Meta:
		verbose_name_plural = 'Reply Comments'

