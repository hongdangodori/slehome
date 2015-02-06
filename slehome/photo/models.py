from django.db import models
from django.contrib.auth.models import User

class Photos(models.Model) :
	link = models.TextField(blank = True)
	pub_date = models.DateField(null=True, blank=True)

	def __str__(self) :
		return self.link

class PhotoComments(models.Model) :
	user = models.ForeignKey(User)
	photo = models.ForeignKey(Photos)
	comments = models.TextField(blank=True)
	pub_date = models.DateField(null=True, blank=True)

	def __str__(self) :
		return self.comments