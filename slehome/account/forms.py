from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# from django.utils.translation import ugettext_lazy as _

from account.models import MyUser, BasicMemberInformation
from account.models import MemberIntro, PhotoLink, Stat
from account.encryption import encrypted_key



# Register 첫 페이지의 기본 정보 입력을 위한 폼
class BasicMemberInformationRegisterForm(forms.Form):
	fullname = forms.CharField(max_length=20, required=True)
	stu_num = forms.IntegerField(required=True)
	auth_key = forms.CharField(max_length=64, required=False)
	no_auth_key = forms.BooleanField(required=False)

	# 가입 신청자가 authorization key를 인증했는지 확인
	def gave_auth_key(self, data):
		# no_auth_key라는 이름의 체크박스에 체크했는지 확인
		checkbox = str(data.get('no_auth_key'))
		if checkbox == "on":
			return False
		else:
			return True

	# 가입 신청자가 BasicMemberInformation 테이블에 존재하는지 확인하고, 존재한다면 그 데이터를 리턴
	def get_member(self, gave_auth_key, data):
		# 이름과 학번으로 존재를 확인
		sent_fullname = data.get('fullname')
		sent_stu_num = int(data.get('stu_num'))
		# auth key를 입력했다면 auth key도 확인
		if gave_auth_key:
			sent_auth_key = data.get('auth_key')
			# BasicMemberInformation 테이블에서 이름, 학번, auth key가 매치되는 row 가져오기를 시도
			try:
				member = BasicMemberInformation.objects.get(
					fullname=sent_fullname,
					stu_num=sent_stu_num,
					auth_key=sent_auth_key
				)
				return member
			# 매치되는 row가 존재하지 않으면 None을 리턴
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

	# auth key 입력 여부와 멤버 인증 여부를 해당 멤버 row에 저장
	def member_validation_update(self, gave_auth_key, member):
		if gave_auth_key:
			member.gave_auth_key = True
		else:
			member.gave_auth_key = False
		member.completed_validation = True
		member.save()



# User 모델과 연결된 가입 폼
class UserRegisterForm(UserCreationForm):
	# Django에 기본으로 존재하는 UserCreationForm을 extend한 것이므로,
	# UserCreationForm에 존재하지 않는 email 필드를 직접 생성해 줌
	email = forms.EmailField(required=True)

	class Meta:
		model = User # User 모델과 연결됨
		fields = ("username", "email", "password1", "password2") # 폼에 포함될 필드를 설정

	def __init__(self, *args, **kwargs):
		super(UserRegisterForm, self).__init__(*args, **kwargs)
		for fieldname in ['username', 'password1', 'password2']:
			self.fields[fieldname].help_text = None # 기본으로 존재하는 help text를 보이지 않게 표시

	# 해당 멤버 계정의 active 여부를 결정
	def is_active_update(self, gave_auth_key, sent_stu_num):
		member = MyUser.objects.get(stu_num=sent_stu_num).user

		# auth key를 입력하였다면 상태를 active로
		if gave_auth_key:
			member.is_active = True
		# auth key를 입력하지 않았다면 상태를 inactive로
		else:
			member.is_active = False
		member.save()



# MyUser 모델과 연결된 가입 폼
class MyUserRegisterForm(forms.ModelForm):
	class Meta:
		model = MyUser # MyUser 모델과 연결됨
		fields = '__all__' # 모델의 모든 필드를 폼으로 생성
		exclude = ['user', 'gave_auth_key', 'level', 'point'] # 이 필드들은 폼으로 만들지 않음



# 패스워드 변경 폼
class ChangePasswordForm(forms.Form):
	current_password = forms.CharField(widget=forms.PasswordInput())
	new_password1 = forms.CharField(widget=forms.PasswordInput())
	new_password2 = forms.CharField(widget=forms.PasswordInput())

	# 유저가 입력한 것이 현재 패스워드가 맞는지 확인
	def check_current_password(self, account_user):
		valid = account_user.check_password(self.cleaned_data['current_password'])
		if valid:
			return True
		else:
			return False

	# 새 패스워드의 입력과 재입력이 일치하는지 확인
	def check_password_match(self):
		password1 = self.cleaned_data['new_password1']
		password2 = self.cleaned_data['new_password2']
		if password1 == password2:
			return True
		else:
			return False

	# 패스워드 변경
	def change_password(self, account_user):
		password = self.cleaned_data['new_password1']
		account_user.set_password(password)
		account_user.save()



# User 모델과 연결된 계정설정 폼
class AccountSettingsUserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ("email",)



# MyUser 모델과 연결된 계정설정 폼
class AccountSettingsMyUserForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = ("nickname", "birthday", "phone_num",)



# 계정설정을 변경할 때 패스워드를 확인하기 위한 폼
class CheckPasswordForm(forms.Form):
	password = forms.CharField(widget=forms.PasswordInput())

	# 패스워드가 맞는지 확인
	def check_password(self, account_user):
		valid = account_user.check_password(self.cleaned_data['password'])		
		if valid:
			return True
		else:
			return False



# MemberIntro 모델과 연결된 자기소개 컨텐츠 폼
class MemberIntroForm(forms.ModelForm):
	class Meta:
		model = MemberIntro
		fields = ('intro',)

# Stat 모델과 연결된 자기소개의 스탯 폼
# class StatForm(forms.ModelForm):
# 	class Meta:
# 		model = Stat
# 		fields = ('stat_name', 'stat_value',)