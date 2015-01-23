from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.db.models import Count
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login

from main.models import Title, MenuList, MenuListForNonmembers
from main.forms import LoginForm
from account.models import MyUser
from main.shared import Navbar

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