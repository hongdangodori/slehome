from django.db import models

# Create your models here.


class Page(models.Model):
	page_name = models.CharField(max_length=20)
	content = models.TextField(null=True)
	author = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')
	new_version = models.BooleanField(default=False)


class FilePath(models.Model):
	# page = models.ForeignKey(Page)
	page_name =models.CharField(max_length=20, null=True)
	upload_path = models.CharField(max_length=30,default='/home/sle/upload/')
	file_name =models.TextField(null=True)
	dummy_name = models.CharField(max_length=20,null=True)

