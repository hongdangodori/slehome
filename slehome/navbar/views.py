# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from navbar.models import Title, MenuList, MenuListForNonmembers
from account.models import MyUser, BasicMemberInformation
from navbar.shared import Navbar

from account.forms import UserRegisterForm, MyUserRegisterForm, BasicMemberInformationRegisterForm
from django.contrib.auth.models import User


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
	gave_auth_key = None
	member_exists = None
	next_page = False
	message = ''
	stu_num = ''

	if request.method == "POST":
		if 'check' in request.POST:
			data = request.POST
			register_form = BasicMemberInformationRegisterForm(data)
			if register_form.is_valid():
				gave_auth_key = register_form.gave_auth_key(data)
				member = register_form.get_member(gave_auth_key, data)
				if member == None:
					message = "No matching member in the Slegizzagi"
				else:
					register_form.member_validation_update(gave_auth_key, member)
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
	message = ""
	user_register_form = ""
	my_user_register_form = ""
	error_dict = ""
	warning = ""

	try:
		member = BasicMemberInformation.objects.get(stu_num=stu_num)
		if member.completed_validation:
			if not member.generated_account:
				url = "main/register_real.html"
				user_register_form = UserRegisterForm()
				my_user_register_form = MyUserRegisterForm(initial={'fullname': member.fullname, 'stu_num': member.stu_num})

				if request.method == "POST":
					if 'create_account' in request.POST:
						data = request.POST.copy()
						data['fullname'] = member.fullname
						data['stu_num'] = member.stu_num
						user_register_form = UserRegisterForm(data)
						my_user_register_form = MyUserRegisterForm(data)
						if user_register_form.is_valid() and my_user_register_form.is_valid():
							user_instance = user_register_form.save(commit=True)
							my_user_instance = my_user_register_form.save(commit=False)
							my_user_instance.user = user_instance
							my_user_instance.save()

							sent_stu_num = member.stu_num
							gave_auth_key = member.gave_auth_key

							user_register_form.is_active_update(gave_auth_key, sent_stu_num)

							member.generated_account = True
							member.save()

							return HttpResponseRedirect("/sle/")
						else:
							error_dict = user_register_form.errors.as_data()
							error_dict.update(my_user_register_form.errors.as_data())
							warning = "▲ Error occurred"
			else:
				url = "main/register_prohibit.html"
				message = "You have already created an account."
		else:
			url = "main/register_prohibit.html"
			message = "You haven't yet completed account validation."
	except (BasicMemberInformation.DoesNotExist):
		url = "main/register_prohibit.html"
		message = "Invalid Approach"

	context_dict = {
		'message': message,
		'user_register_form': user_register_form,
		'my_user_register_form': my_user_register_form,
		"error_dict": error_dict,
		'warning': warning,
	}

	context_dict.update(navbar.context_dict())

	return render(request, url, context_dict)


	#context = RequestContext(request, context_dict)

	#return HttpResponse(template.render(context))
