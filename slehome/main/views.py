# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect
from django.http import *

from django.contrib import auth
from django.core.context_processors import csrf

from navbar.shared import Navbar



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

	if navbar.user.is_authenticated():
		url = "main/main_index.html"
	else:
		url = "main/main_onepage.html"

	context_dict = {}
	context_dict.update(navbar.context_dict())
	
	return render(request, url, context_dict)