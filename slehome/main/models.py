from django.db import models

class Title(models.Model):
	name = models.CharField(max_length=50)
	num = models.IntegerField(max_length=2, unique=True, default=0)
	def __str__(self):
		return self.name

class MenuList(models.Model):
	menu = models.CharField(max_length=20)
	link = models.CharField(max_length=70)
	display_ord = models.IntegerField(max_length=2)
	display = models.BooleanField(default=True)
	def __str__(self):
		return self.menu

class MenuListForNonmembers(models.Model):
	menu = models.CharField(max_length=20)
	link = models.CharField(max_length=70)
	display_ord = models.IntegerField(max_length=2)
	display = models.BooleanField(default=True)
	def __str__(self):
		return self.menu