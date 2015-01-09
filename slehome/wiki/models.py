from django.db import models

# Create your models here.


class Page(models.Model):
	page_name = models.CharField(max_length=20)
	content = models.TextField(null=True)
	author = models.IntegerField(default=0)
	pub_date = models.DateTimeField('date published')


class FilePath(models.Model):
	page = models.ForeignKey(Page)
	file_path = models.TextField(null=True)

