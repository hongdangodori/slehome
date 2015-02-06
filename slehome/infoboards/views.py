from django.shortcuts import render
from django.template import RequestContext
from django.template import loader
from django.http import HttpResponse
import simplejson
from django.core import serializers
from django.forms.models import model_to_dict
from account.models import MyUser

from django.contrib.auth.decorators import login_required
from navbar.shared import NavbarForMembers


def test(request):
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	context_dict = {'user':request.user}
	context_dict.update(navbar.context_dict())
	url = "infoboards/test.html"
	
	
	return render(request, url, context_dict)

def test2(request):
		#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	name = request.GET['name']
	age = request.GET['age']

	context = {'name':name, 'age':age}
	context.update(navbar.context_dict())
	
	url = 'infoboards/test2.html'
	return render(request, url, context)
	# return HttpResponse(simplejson.dumps({'name':data.nickname, 'age':age}), content_type="application/json")

def ellip_test(request):
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################


	context = {}
	context.update(navbar.context_dict())
	
	url = 'infoboards/ellip_test.html'
	return render(request, url, context)