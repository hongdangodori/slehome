from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from main.shared import NavbarForMembers

@login_required
def members_index(request):
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()

	###unique part###
	context_dict = {}
	template = loader.get_template('members/members_index.html')
	###unique part###

	context_dict.update(navbar.context_dict())
	context = RequestContext(request, context_dict)

	return HttpResponse(template.render(context))