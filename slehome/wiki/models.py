from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Page(models.Model):
	author = models.ForeignKey(User)
	page_name = models.CharField(max_length=20)
	content = models.TextField(null=True)
	pub_date = models.DateTimeField('date published')
	new_version = models.BooleanField(default=False)
	def __str__(self):
		return self.page_name


class FilePath(models.Model):
	# page = models.ForeignKey(Page)
	page_name =models.CharField(max_length=20, null=True)
	upload_path = models.CharField(max_length=30,default='/home/sle/upload/')
	file_name =models.TextField(null=True)
	dummy_name = models.CharField(max_length=20,null=True)
	def __str__(self):
		return self.file_name

