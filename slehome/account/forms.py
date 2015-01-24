from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

from account.models import MyUser, BasicMemberInformation

from django.utils.translation import ugettext_lazy as _

class LoginForm(forms.Form):
	user_id = forms.CharField(label='User ID', max_length=50, widget=forms.TextInput)
	user_password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)

class BasicMemberInformationRegisterForm(forms.ModelForm):

	class Meta:
		model = BasicMemberInformation
		fields = '__all__'
		#widgets = {
        #   "fullname" : forms.TextInput(attrs={"class" : "form-control"}),
		#}
		labels = {
			'fullname': _('Name'),
			'stu_num': _('Student Number'),
			'auth_key': _('Authorization Key')
		}

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        for fieldname in ['username', 'password1', 'password2']:
            self.fields[fieldname].help_text = None

    def save(self, commit=True):
        user = super(UserRegisterForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class MyUserRegisterForm(forms.ModelForm):

	class Meta:
		model = MyUser
		fields = '__all__' #('user', 'fullname', 'nickname', 'stu_num', 'phone_num')
		exclude = ['user']

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