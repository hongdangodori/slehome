from django.db import models

# Create your models here.
class FreeBoard(models.Model):
	user = models.CharField(max_length=20, blank=True)
	category = models.CharField(max_length=30, blank=True)
	title = models.CharField(max_length=50, blank=True)
	contents = models.TextField(blank = True)
	pub_date = models.DateField(null=True, blank=True)
	hits = models.IntegerField(null=True, blank=True)
	file_path = models.CharField(max_length=50, null=True, blank=True)
	like = models.IntegerField(null=True, blank=True)

	def __str__(self):
		return self.title

class LikeArticle(models.Model):
	user = models.CharField(max_length=20, blank=True)
	article = models.ForeignKey('FreeBoard')
	like = models.BooleanField(default=False)
 
	def is_like(self):
		return self.like