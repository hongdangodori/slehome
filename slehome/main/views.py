from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from main.models import Title, MenuList, MenuListForNonmembers
from account.models import MyUser
from main.shared import Navbar

from account.forms import UserRegisterForm, MyUserRegisterForm, BasicMemberInformationRegisterForm

def main_index(request):
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'login' in request.POST:
			navbar.user_login()
			navbar.user_setting()
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###unique part###
	context_dict = {}
	template = loader.get_template('main/main_index.html')
	###unique part###

	context_dict.update(navbar.context_dict())
	context = RequestContext(request, context_dict)

	return HttpResponse(template.render(context))

def register_one(request):
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'login' in request.POST:
			navbar.user_login()
			navbar.user_setting()
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###unique part###
	basic_member_information_register_form = BasicMemberInformationRegisterForm(initial={'auth_key': ''})
	user_register_form = UserRegisterForm()
	my_user_register_form = MyUserRegisterForm()

	context_dict = {
		'basic_member_information_register_form': basic_member_information_register_form,
		'user_register_form': user_register_form,
		'my_user_register_form': my_user_register_form,
	}
	template = loader.get_template('main/register_one.html')
	###unique part###

	context_dict.update(navbar.context_dict())
	context = RequestContext(request, context_dict)

	return HttpResponse(template.render(context))

def register_two(request):
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'login' in request.POST:
			navbar.user_login()
			navbar.user_setting()
		if 'logout' in request.POST:
			navbar.user_logout()
			navbar.user_setting()

	###unique part###
	user_register_form = UserRegisterForm()
	my_user_register_form = MyUserRegisterForm()

	context_dict = {
		'user_register_form': user_register_form,
		'my_user_register_form': my_user_register_form,
	}
	template = loader.get_template('main/register_two.html')
	###unique part###

	context_dict.update(navbar.context_dict())
	context = RequestContext(request, context_dict)

	return HttpResponse(template.render(context))