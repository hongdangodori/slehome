from django.db import models
from django.contrib.auth.models import User
from account.encryption import encrypted_key

class MyUser(models.Model):
	user = models.OneToOneField(User, related_name='myuser')
	fullname = models.CharField(max_length=20)
	nickname = models.CharField(max_length=20, unique=True)
	stu_num = models.IntegerField(max_length=8, unique=True)
	phone_num = models.CharField(max_length=11)

class BasicMemberInformation(models.Model):
	fullname = models.CharField(max_length=20)
	stu_num = models.IntegerField(max_length=8, unique=True)
	auth_key = models.CharField(max_length=64, default=encrypted_key())
	def __str__(self):
		return self.fullname