from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from wiki.models import Page, FilePath
import datetime
# Create your views here.


def view_page(request, page_name=''):
	if page_name == '':
		page_name = 'FrontPage'

	try:
		page = Page.objects.get(page_name=page_name)
	except Page.DoesNotExist:
		return render(request,"create.html",{"page_name":page_name})
	
	content = page.content
	pub_date=page.pub_date
	c={"page_name":page_name,"content":content,"pub_date":pub_date}	
	
	return render(request,"view.html",c)

def edit_page(request,page_name):
	try:
		page = Page.objects.get(page_name=page_name)
		content = page.content
	except Page.DoesNotExist:
		content = ""
	c={"page_name":page_name,"content":content}
	c.update(csrf(request))
	return render(request,"edit.html",c)

def save_page(request,page_name):
	content=request.POST["content"]
	try:
		page=Page.objects.get(page_name=page_name)
		page.content=content
		page.pub_date=datetime.datetime.now()
	except Page.DoesNotExist:
		page = Page(page_name=page_name, content=content, pub_date=datetime.datetime.now())
	page.save()
	return HttpResponseRedirect("/sle/wiki/"+page_name+"/")