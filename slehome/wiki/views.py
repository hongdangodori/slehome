from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from wiki.models import Page, FilePath
from django.db.models import Q
import datetime
# Create your views here.


def view_page(request, page_name=''):
	if page_name == '':
		page_name = 'FrontPage'

	try:
		page = Page.objects.filter(page_name=page_name)
		if len(page) > 0 :
			page = page[len(page)-1]
	except Page.DoesNotExist:
		return render(request,"create.html",{"page_name":page_name})
	
	content = page.content
	pub_date=page.pub_date
	c={"page_name":page_name,"content":content,"pub_date":pub_date}	
	
	return render(request,"view.html",c)

def edit_page(request,page_name):
	try:
		page = Page.objects.filter(page_name=page_name)
		if len(page) > 0 :
			page = page[len(page)-1]
		content = page.content
	except Page.DoesNotExist:
		content = ""
	c={"page_name":page_name,"content":content}
	c.update(csrf(request))
	return render(request,"edit.html",c)

def save_page(request,page_name):
	content=request.POST["content"]
	page = Page(page_name=page_name, content=content, pub_date=datetime.datetime.now())

	page.save()
	return HttpResponseRedirect("/sle/wiki/"+page_name+"/")

def search_page(request):
	search_key=request.POST["search_key"]
	search_key_list=search_key.split()
	page_object=Page.objects
	page_list=[]

	test=""
	page=page_object.filter(page_name=search_key)
	if len(page) > 0 :
		page = page[len(page)-1]
		c={"page_name":page.page_name , "content":page.content, "pub_date":page.pub_date}	
		return render(request,"view.html",c)

	else:
		page=page_object
		for word in search_key_list:
			page=page.filter(Q(page_name__contains=word) | Q(content__contains=word))
			page_list += page

		temp_list = list(set(page_list))		
		page_list = []

		for element in temp_list:
			count = 0
			if len(page_list) == 0 :
		 		page_list.append(element)
			else:
		 		for temp in page_list:
		 			if temp.page_name == element.page_name:
		 				count = 1
		 				break
		
		 		if count == 0:
		 			page_list.append(element)

		c={"page":page_list , "search_key":search_key}	
	
		return render(request,"search.html",c)	

