from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from account.models import MyUser, BasicMemberInformation

from django.utils.translation import ugettext_lazy as _

from django.shortcuts import get_object_or_404
from account.models import MyUser, BasicMemberInformation


class BasicMemberInformationRegisterForm(forms.Form):
	fullname = forms.CharField(max_length=20, required=True)
	stu_num = forms.IntegerField(required=True)
	auth_key = forms.CharField(max_length=64, required=False)
	no_auth_key = forms.BooleanField(required=False)

	def gave_auth_key(self, data):
		checkbox = str(data.get('no_auth_key'))
		if checkbox == "on":
			return False
		else:
			return True

	def get_member(self, gave_auth_key, data):
		sent_fullname = data.get('fullname')
		sent_stu_num = int(data.get('stu_num'))
		if gave_auth_key:
			sent_auth_key = data.get('auth_key')
			try:
				member = BasicMemberInformation.objects.get(
					fullname=sent_fullname,
					stu_num=sent_stu_num,
					auth_key=sent_auth_key
				)
				return member
			except (BasicMemberInformation.DoesNotExist):
				return None
		else:
			try:
				member = BasicMemberInformation.objects.get(
					fullname=sent_fullname,
					stu_num=sent_stu_num,
				)
				return member
			except (BasicMemberInformation.DoesNotExist):
				return None

	def member_validation_update(self, gave_auth_key, member):
		if gave_auth_key:
			member.gave_auth_key = True
		else:
			member.gave_auth_key = False
		member.completed_validation = True
		member.save()


class UserRegisterForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)

		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None

	def is_active_update(self, gave_auth_key, sent_stu_num):
		member = MyUser.objects.get(stu_num=sent_stu_num).user

		if gave_auth_key:
			member.is_active = True
		else:
			member.is_active = False
		member.save()


	"""def save(self, commit=True):
		e = super(UserRegisterForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user"""


class MyUserRegisterForm(forms.ModelForm):

	def __init__(self, *args, **kwargs):
		super(MyUserRegisterForm, self).__init__(*args, **kwargs)
		self.fields['fullname'].widget.attrs['readonly'] = True
		self.fields['stu_num'].widget.attrs['readonly'] = True

	class Meta:
		model = MyUser
		fields = '__all__' #('user', 'fullname', 'nickname', 'stu_num', 'phone_num')
		exclude = ['user', 'gave_auth_key']


	"""def save(self, commit=True):
		myuser = super(MyUserRegisterForm, self).save(commit=False)
		myuser = User(user=)
		if commit:
			user.save()
		return user"""