from django.db import models
from django.contrib.auth.models import User
from account.encryption import encrypted_key
from django.core.validators import MinValueValidator, MaxValueValidator



# Django 기본 User Model을 Extend한 것
class MyUser(models.Model):
	user = models.OneToOneField(User, related_name='myuser')
	fullname = models.CharField(max_length=20)
	nickname = models.CharField(max_length=10, unique=True)
	stu_num = models.IntegerField(max_length=8, unique=True)
	phone_num = models.CharField(max_length=11)
	birthday = models.CharField(max_length=6)
	point = models.IntegerField(default=0)
	level = models.IntegerField(default=1)

	def __str__(self):
		return self.nickname



# 슬기짜기 멤버에 대한 간단한 정보가 들어 있는 테이블 (관리자가 직접 입력해야 함)
class BasicMemberInformation(models.Model):
	fullname = models.CharField(max_length=20)
	stu_num = models.IntegerField(max_length=8)
	auth_key = models.CharField(max_length=64, default=encrypted_key())
	completed_validation = models.BooleanField(default=False)
	gave_auth_key = models.BooleanField(default=False)
	generated_account = models.BooleanField(default=False)

	def __str__(self):
		return self.fullname



# 계정 설정 메뉴의 서브메뉴 리스트
class AccountSettingsMenuList(models.Model):
	menu = models.CharField(max_length=20)
	link = models.CharField(max_length=70, blank=True)
	display_ord = models.IntegerField(max_length=2)
	display = models.BooleanField(default=True)

	def __str__(self):
		return self.menu



# 멤버 자기소개
class MemberIntro(models.Model):
	user = models.OneToOneField(User, related_name='memberintro')
	intro = models.TextField()

	def __str__(self):
		return self.intro


# 멤버 자기소개용 사진 링크
class PhotoLink(models.Model):
	member_intro = models.OneToOneField(MemberIntro, related_name='photolink')
	file_name = models.CharField(max_length=64)
	upload_path = models.CharField(max_length=64, default='/home/sle/media/member/')

	def __str__(self):
		return self.file_name


# 멤버 자기소개용 스텟
class Stat(models.Model):
	member_intro = models.ForeignKey(MemberIntro)
	stat_name = models.CharField(max_length=15)
	stat_value = models.IntegerField(validators=[MinValueValidator(0),
												MaxValueValidator(10)])

	def __str__(self):
		return self.stat_name