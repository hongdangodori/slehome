from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from main.models import Title, MenuList, MenuListForNonmembers
from main.forms import LoginForm
from account.models import MyUser

class Navbar:
	title = Title.objects.get(num=0)
	form = LoginForm()
	error_state = None
	menu_list = MenuList.objects.annotate(Count('menu'))\
						.order_by('display_ord')
	menu_list_for_nonmembers = MenuListForNonmembers.objects.annotate(Count('menu'))\
													.order_by('display_ord')
	base_path = "http://54.169.79.59/sle/"

	def __init__(self, request):
		self.request = request

	def get_current_path(self):
		self.current_path = self.request.path

	def user_setting(self):
		self.user = self.request.user
		if self.user is not None:
			if not self.user.is_authenticated():
				self.nickname = "guest"
			else:
				self.nickname = self.user.myuser.nickname

	def user_login(self):
		self.form = LoginForm(self.request.POST)
		if self.form.is_valid():
			user_id = self.form.cleaned_data['user_id']
			user_password = self.form.cleaned_data['user_password']
			self.user = authenticate(username=user_id, password=user_password)
			if self.user is not None:
				login(self.request, self.user)
				return HttpResponseRedirect('/sle')
			else:
				self.error_state = "wrong_id_or_password"
		else:
			self.error_state = "forms_not_filled"

	def user_logout(self):
		logout(self.request)
		return HttpResponseRedirect('/sle')

	def context_dict(self):
		context_dict = {
			'title': self.title,
			'menu_list': self.menu_list,
			'menu_list_for_nonmembers': self.menu_list_for_nonmembers,
			'user': self.user,
			'nickname': self.nickname,
			'form': self.form,
			'error_state': self.error_state,
			'current_path': self.current_path,
			'base_path': self.base_path,
		}
		return context_dict

class NavbarForMembers:
	title = Title.objects.get(num=0)
	menu_list = MenuList.objects.annotate(Count('menu'))\
						.order_by('display_ord')
	base_path = "http://54.169.79.59/sle/"

	def __init__(self, request):
		self.get_current_path()
		self.user_setting()
		self.request = request

	def get_current_path(self):
		self.current_path = self.request.path

	def user_setting(self):
		self.user = self.request.user
		if self.user is not None:
			if not self.user.is_authenticated():
				self.nickname = "guest"
			else:
				self.nickname = self.user.myuser.nickname

	def user_logout(self):
		logout(self.request)
		return HttpResponseRedirect('/sle')

	def context_dict(self):
		context_dict = {
			'title': self.title,
			'menu_list': self.menu_list,
			'user': self.user,
			'nickname': self.nickname,
			'current_path': self.current_path,
			'base_path': self.base_path,
		}
		return context_dict

	def call_main_nav(self):
		self.get_current_path()
		self.user_setting()

		context={}
		context.update(self.context_dict())
		return context
