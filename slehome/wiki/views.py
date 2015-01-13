from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from wiki.models import Page, FilePath
from django.db.models import Q
import datetime
# Create your views here.


def view_page(request, page_name='',page_num=''):
	is_history = False
	if page_name == '':
		page_name = 'FrontPage'
	
	page = Page.objects.filter(page_name=page_name)
	if len(page) > 0 :
		if page_num != '' and page_num != '1':
			try:
				is_history = True
				page = page[len(page)-int(page_num)]
			except:
				c={"alert":"페이지가 없습니다."}
				return render(request,"alert.html",c)
		else:
			page = page[len(page)-1]
	else:
		return render(request,"create.html",{"page_name":page_name})

	content = page.content
	pub_date=page.pub_date
	c={"page_name":page_name,"content":content,"pub_date":pub_date,"is_history":is_history}	 
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
	page=Page.objects.filter(page_name=page_name)
	page=page[len(page)-1]
	if page.content != content :
		page.new_version=False
		page.save()
		page = Page(page_name=page_name, content=content, pub_date=datetime.datetime.now(),new_version=True)
		page.save()
		
	return HttpResponseRedirect("/sle/wiki/"+page_name+"/")

def search_page(request):
	search_key=request.POST["search_key"]
	search_key_list=search_key.split()
	page_object=Page.objects
	page_list=[]

	# test=""
	page=page_object.filter(page_name=search_key)
	if len(page) > 0 :
		page = page[len(page)-1]
		return HttpResponseRedirect("/sle/wiki/"+page.page_name+"/")

	else:
		page=page_object
		for word in search_key_list:
			page=page.filter(Q(page_name__contains=word) | Q(content__contains=word))
			# page_list += page

		page_list += page
		temp_list = list(set(page_list))		
		page_list = []

		for temp in temp_list:
			count = 0
			if temp.new_version == True :
				if len(page_list) == 0 :
			 		page_list.append(temp)
				else:
			 		for p in page_list:
			 			if p.page_name == temp.page_name:
			 				count = 1
			 				break
			
			 		if count == 0:
			 			page_list.append(temp)

		c={"page":page_list , "search_key":search_key}	
	
		return render(request,"search.html",c)	


def history_page(request,page_name=''):
	if page_name == '':
		c={'alert':'페이지 이름이 없습니다.'}
		return render(request,"alert.html",c)

	else:
		page_list = Page.objects.filter(page_name=page_name)
		count = 0
		p = []
		for page in page_list[::-1]:
			count += 1
			p.append({"pub_date":page.pub_date,"count":count})

		c={"page":p,"page_name":page_name}
		return render(request,"history.html",c)