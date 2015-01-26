# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from main.models import Title, MenuList, MenuListForNonmembers
from account.models import MyUser, BasicMemberInformation
from main.shared import Navbar

from account.forms import UserRegisterForm, MyUserRegisterForm, BasicMemberInformationRegisterForm
from django.core.urlresolvers import reverse

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

	###############################################################
	context_dict = {}
	template = loader.get_template('main/main_index.html')
	###############################################################

	context_dict.update(navbar.context_dict())
	context = RequestContext(request, context_dict)

	return HttpResponse(template.render(context))


def register_index(request):
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

	###############################################################
	basic_member_information_register_form = BasicMemberInformationRegisterForm(initial={'auth_key': ''})
	has_auth_key = None
	member_exists = None
	next_page = False
	message = ''
	stu_num = ''

	if request.method == "POST":
		if 'register_index' in request.POST:
			register_form = BasicMemberInformationRegisterForm(request.POST)
			if register_form.is_valid():
				data = request.POST
				has_auth_key = register_form.has_auth_key(data)
				member_exists = register_form.member_exists(has_auth_key, data)
				if member_exists == None:
					message = "No matching member in the Slegizzagi"
				else:
					member = member_exists
					next_page = True
					stu_num = str(member.stu_num)
			else:
				message = "Check your answers again"
				#state = register_form.errors

	context_dict = {
		'stu_num': stu_num,
		'next_page': next_page,
		'message': message,
		'basic_member_information_register_form': basic_member_information_register_form,
	}
	context_dict.update(navbar.context_dict())

	"""if next_page == True:
		url = "main/register_real.html"
		#return HttpResponseRedirect('proceed/')
		#return HttpResponseRedirect('/sle/register/'+str(member.stu_num))
	else:"""
	url = "main/register_index.html"
	return render(request, url, context_dict)



def register_real(request, stu_num):
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

	###############################################################
	user_register_form = UserRegisterForm()
	my_user_register_form = MyUserRegisterForm()

	context_dict = {
		'user_register_form': user_register_form,
		'my_user_register_form': my_user_register_form,
	}
	template = loader.get_template('main/register_real.html')

	context_dict.update(navbar.context_dict())

	url = "main/register_real.html"
	#else:
	#	url = "main/register_prohibit.html"
	return render(request, url, context_dict)


	#context = RequestContext(request, context_dict)

	#return HttpResponse(template.render(context))