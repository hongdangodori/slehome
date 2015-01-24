from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from account.models import MyUser, BasicMemberInformation

"""class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
"""

class MyUserRegisterForm(forms.ModelForm):
	class Meta:
		model = MyUser
		fields = '__all__' #('user', 'fullname', 'nickname', 'stu_num', 'phone_num')

	"""def clean_user(self):
	    username
        email = self.cleaned_data['user']
		if User.objects.get(email__iexact=user_email):
            return User.objects.get(email__iexact=user_email)
        return None"""

	"""def save(self, commit=True):
        user = super(MyUserRegisterForm, self).save(commit=False)
        if commit:
            user.save()
        return user"""

class BasicMemberInformationRegisterForm(forms.ModelForm):
	class Meta:
		model = BasicMemberInformation
		fields = ('fullname', 'stu_num', 'auth_key')