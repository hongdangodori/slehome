# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect, HttpResponse
from wiki.models import Page, FilePath
from django.db.models import Q
import datetime
import os, sys
from django.core.servers.basehttp import FileWrapper
import codecs

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
				c={"alert":"페이지가 없습니다.",'location':'/sle/wiki/FrontPage'}
				return render(request,"alert.html",c)
		else:
			page = page[len(page)-1]
	else:
		return render(request,"create.html",{"page_name":page_name})

	content = page.content
	pub_date=page.pub_date

	file_list = []
	file_path = FilePath.objects.filter(page_name=page_name)
	count = 0
	if len(file_path) > 0:
		for f_p in file_path:
			count += 1
			file_list.append({'file_name':f_p.file_name,'upload_path':f_p.upload_path,'count':count})

	c={"page_name":page_name,"content":content,"pub_date":pub_date,"is_history":is_history,"file_list":file_list}	 
	return render(request,"view.html",c)

def edit_page(request,page_name):
	page = Page.objects.filter(page_name=page_name)
	if len(page) > 0 :
		page = page[len(page)-1]
		content = page.content
	else: 
		content = ""
	c={"page_name":page_name,"content":content}
	c.update(csrf(request))
	return render(request,"edit.html",c)

def save_page(request,page_name):
	content=request.POST["content"]
	page=Page.objects.filter(page_name=page_name)

	if len(page) > 0:
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

def upload_page(request,page_name=''):
	if request.method == 'POST':
		UPLOAD_DIR = '/home/sle/upload'
		if 'file' in request.FILES:
			file = request.FILES['file']
			file_name = file._name

		fp = open('%s/%s' % (UPLOAD_DIR, file_name.encode('utf-8')) , 'wb')
		for chunk in file.chunks():
			fp.write(chunk)

		fp.close()

		f = FilePath(page_name=page_name, upload_path=UPLOAD_DIR, file_name=file_name.encode('utf-8'))
		f.save()

		c={'alert': '올리신 '+file_name+' 파일이 업로드 되었습니다.','location':'/sle/wiki/'+page_name}
		return render(request,"alert.html",c)

	else:
		c={'alert':'파일 업로드가 실패했습니다.','location':'/sle/wiki/'+page_name}
		return render(request,"alert.html",c)


def download_page(request,page_name='',file_num=''):
	if page_name == '' or file_num == '':
		c={'alert':'잘못된 다운로드 요청입니다.','location':'/sle/wiki/'+page_name}
		return render(request,"alert.html",c)

	file_data_list = FilePath.objects.filter(page_name=page_name)
	if len(file_data_list) == 0:
		c={'alert':'파일이 없습니다.','location':'/sle/wiki/'+page_name}
		return render(request,"alert.html",c)

	file_data = file_data_list[int(file_num)-1]
	
	full_file_name = file_data.upload_path +'/'+ str(file_data.file_name.encode("utf-8"))
	f=open(full_file_name,'rb')
	wrapper = FileWrapper(f)

	response = HttpResponse(wrapper, content_type='Application/octet-stream; charset=utf-8')
	response['Content-Disposition'] = 'attachment; filename=' + "\""+file_data.file_name.encode("utf-8").decode('"ISO-8859-1"')+ "\""
	response['Content-Length'] = int(os.path.getsize(full_file_name))
	f.close()
	# c={'content':'attachment; filename=' + str(file_data.file_name.encode("utf-8").decode('utf-8'))}
	# return render(request,'view.html',c)
	return response
	# if page_name == '' or file_num == '':
	# 	c={'alert':'잘못된 다운로드 요청입니다.'}
	# 	return render(request,"alert.html",c)

	# file_data_list = FilePath.objects.filter(page_name=page_name)

	# file_data = file_data_list[int(file_num)-1]
	# filename =file_data.file_name

	# file_path = reduce(os.path.join, (file_data.upload_path, filename))
	# if os.path.exists(file_path) and os.path.isfile(file_path):
	# 	with open(file_path, 'rb') as fp:
	# 		response = HttpResponse(fp.read())
	# 	content_type, encoding = mimetypes.guess_type(filename)
	# 	if content_type is None:
	# 		content_type = 'application/octet-stream'
	# 	response['Content-Type'] = content_type
	# 	response['Content-Length'] = str(os.stat(file_path).st_size)
	# if encoding is not None:
	# 	response['Content-Encoding'] = encoding
	# if u'WebKit' in request.META.get('HTTP_USER_AGENT', u'Webkit'):
	# 	filename_header = 'filename="%s"' % filename.encode('utf-8')
	# elif u'MSIE' in request.META.get('HTTP_USER_AGENT', u'MSIE'):
	# 	filename_header = ""
	# else:
	# 	filename_header = 'filename*=UTF-8\'\'%s' % urllib.quote(filename.encode('utf-8'))
	
	# response['Content-Disposition'] = 'attachment; ' + filename_header
	# return response
	

# Create your views here.