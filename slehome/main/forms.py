from django import forms

class LoginForm(forms.Form):
	user_id = forms.CharField(label='User ID', max_length=50, widget=forms.TextInput)
	user_password = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)