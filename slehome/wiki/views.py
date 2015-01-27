# -*- coding: utf-8 -*-
from django.shortcuts import render	#template로 넘어가는데 사용되는 메소드
from django.core.context_processors import csrf	#form을 통해 data를 넘겨받을때 사용해야 하는 것
from django.http import HttpResponseRedirect, HttpResponse #HttpResponse를 위해 사용
from wiki.models import Page, FilePath #wiki에 사용되는 model들
from django.db.models import Q 	#django의 model에서 필요한 자료를 뽑아낼 때 사용됨 or나 and가 가능하게 해주는 기능
import datetime	#시간 정보를 뽑아내는데 사용됨
import os, sys #file download와 upload를 구현하는데 상용됨
from django.core.servers.basehttp import FileWrapper #download를 위해 사용됨
import random, string	#file upload시 임의의 문자열을 생성해서 파일을 저장하도록 만듬 (중복된 이름을 가진 파일의 경우 업로드시 겹치기 때문에 사용된다.)

from wiki.markdown import markdown, ContentEdit 	#wiki의 markdown 기능을 위해 사용됨 (자체 제작)
from navbar.shared import Navbar
from instagram.client import InstagramAPI # instagram을 사용하기 위한 module 차후에 옮길 예정

def view_page(request, page_name='',page_num=''): #wiki page를 보여주는 역할을 하는 method이다. 
										  #page_name은 페이지 이름, page_num은 페이지의 번호로 페이지의 수정 버전같은 것이다.
	is_history = False	#과거 페이지인지 아닌지를 확인, 과거 페이지일 경우 수정 및 파일 업로드가 불가능하다.
	if page_name == '':	#page_name이 정해져 있지 않을 경우 FrontPage로 간다.
		page_name = 'FrontPage'
	
	page = Page.objects.filter(page_name=page_name)	#model에서 page_name에 해당하는 page를 불러온다.
	if len(page) > 0 : #page가 존재할 경우
		if page_num != '' and page_num != '1':
			try:
				is_history = True	#page가 history에 포함된 예전 page일 경우 True 로 바꿔준다.
				page = page[len(page)-int(page_num)]	#그리고 그 page를 연결한다.
			except:
				c={"alert":"페이지가 없습니다.",'location':'/sle/wiki/FrontPage'}
				return render(request,"wiki/alert.html",c)
		else:
			page = page[len(page)-1]	#가장 최근 page를 불러온다.
	else:	#page가 존재하지 않을 경우 
		return render(request,"wiki/create.html",{"page_name":page_name}) #새로운 page를 만들도록 한다.

	md = markdown(page_name, page.content)	#page의 content를 markdown처리해준다.
	content = md['content']	# markdown 처리된 content를 불러온다.
	context = md['context'] # 목차를 불러온다.
	pub_date=page.pub_date #page의 생성 시간 정보를 불러온다.

	file_list = []
	file_path = FilePath.objects.filter(page_name=page_name) #page와 연결되어있는 파일 목록들을 불러온다.
	count = 0
	if len(file_path) > 0:	#연결되어있는 파일이 여러 개일 경우
		for f_p in file_path:
			count += 1 #파일 count를 세어준다. 나중에 파일 목록을 통해 다운로드 할 때 필요하다.
			file_list.append({'file_name':f_p.file_name,'upload_path':f_p.upload_path,'count':count}) #파일 목록에 추가한다.

	c={"page_name":page_name,"context":context,"content":content,"pub_date":pub_date,"is_history":is_history,"file_list":file_list}	 #template로 보낼 정보들을 모아놓는다.
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()
	c.update(navbar.context_dict())		

	return render(request,"wiki/view.html",c) #template로 연결한다.

def edit_page(request,page_name,section='0'): #page의 내용을 변경하기 위한 method이다.
	section = int(section) #부분 편집을 위한 변수다.
	page = Page.objects.filter(page_name=page_name) #page_name을 가지고 page에 대한 정보를 불러온다.
	if len(page) > 0 :	#page가 존재할 경우
		page = page[len(page)-1]	#page중 가장 최근 페이지를 수정해야 하기 때문에 가장 최근 페이지에 대한 정보를 불러온다.
		content = page.content 		#page의 content를 불러온다.
		if section > 0 :			#section을 이용하여 content부분 중 어느 부분인지를 확인한다.
									#section이 0일 경우에는 전체 content를 불러와서 변경한다.
			md = markdown(page_name, content)['edit'] #edit를 위해 markdown 함수에서 처리해서 가져온다.
			content = ContentEdit(content, md[section]['line'], md[section]['next_line']) #수정할 부분을 가져온다.
	else: 	#page가 없을 경우 
		content = "" 

	c={"page_name":page_name,"content":content,"section":str(section)} 
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()
	c.update(navbar.context_dict())		
	
	c.update(csrf(request)) #form으로 넘기기 때문에 보안상 이유로 csrf처리를 해서 보낸다.
	return render(request,"wiki/edit.html",c)	#template로 넘김

def save_page(request,page_name,section='0'): #수정하거나 새로 만든 page를 저장하는 역할을 하는 method
	content=request.POST["content"]	#content를 post로 받아온다.
	section = int(section)	#section을 int로 바꿔준다..
	page=Page.objects.filter(page_name=page_name) #해당 page에 대한 정보를 가져온다.
	cur_content = ''

	if len(page) > 0:
		page=page[len(page)-1]	#가장 최근 page를 불러온다.
		if section == 0 :
			cur_content = page.content #section이 0일경우 전체 page의 content를 변경한다.
		elif section > 0 :	#부분 편집을 할 부분을 가져옴
			md = markdown(page_name, page.content)['edit']	#부분 편집을 할 부분을 가져오는 처리
			cur_content = ContentEdit(page.content, md[section]['line'], md[section]['next_line']) 
		if cur_content != content :	#page 수정이 이루어졌을 경우
			page.new_version=False	#이전 page의 version을 이전 버전으로 변경
			page.save()	#예전 page를 그대로 저장
		else :
			return HttpResponseRedirect("/sle/wiki/page/"+page_name+"/") #page가 변경 되지 않을 경우 원래 page view로 이동
		content = page.content.replace(cur_content, content, 1) #page content를 변경함
			
	page = Page(page_name=page_name, content=content, pub_date=datetime.datetime.now(),new_version=True) #새로운 page 객체를 생성해서 저장 history를 위해 페이지가 수정될 때마다 새로운 버전으로서 저장되게 만듬
	page.save()	
	return HttpResponseRedirect("/sle/wiki/page/"+page_name+"/") #page view로 이동

def search_page(request):	#page 검색 기능을 담당하는 method
	search_key=request.POST["search_key"]	#검색을 위한 키워드들을 받아온다.
	search_key_list=search_key.split()	#키워드를 단어 단위로 분할
	page_object=Page.objects	#page들의 모델을 찾아온다.
	page_list=[]

	# test=""
	page=page_object.filter(page_name=search_key) #일단 검색어 자체로 page를 검색해본다.
	if len(page) > 0 :	#검색어와 동일한 이름의 page가 존재할 경우 page의 view로 이동
		page = page[len(page)-1]
		return HttpResponseRedirect("/sle/wiki/page/"+page.page_name+"/")

	else:	#없을 경우 검색어를 구성하는 키워드들을 이용하여 검색을 한다.
		page=page_object
		for word in search_key_list: #키워드들을 이용하여 제목과 내용을 돌아보며 찾도록 한다.
			page=page.filter(Q(page_name__contains=word) | Q(content__contains=word)) 
			# page_list += page

		page_list += page #검색한 page들의 중복을 피하기 위해 set으로 변경하여 처리한다.
		temp_list = list(set(page_list))
		page_list = []

		for temp in temp_list:	#다음으로 페이지들 중 가장 최신 페이지들만을 뽑아내도록 하는 과정이다.
			count = 0
			if temp.new_version == True :	#new_version일 경우에만 추가한다.
				page_list.append(temp)
				# if len(page_list) == 0 :
			 # 		page_list.append(temp)
				# else:
			 # 		for p in page_list:
			 # 			if p.page_name == temp.page_name: #이 부분은 필요가 없을 것 같다. 
			 # 				count = 1
			 # 				break
			
			 # 		if count == 0:
			 # 			page_list.append(temp)

		c={"page":page_list , "search_key":search_key}	#search page에 띄워주기 위한 정보들
		navbar = Navbar(request)
		navbar.get_current_path()
		navbar.user_setting()
		c.update(navbar.context_dict())		
	
		return render(request,"wiki/search.html",c)	#search페이지로 이동한다.


def history_page(request,page_name=''): #history를 보기 위한 기능을 제공해주는 method
	if page_name == '':
		c={'alert':'페이지 이름이 없습니다.'} #page_name이 없을 경우 history를 보여주지 않고 이전 페이지로 돌아간다.
		return render(request,"wiki/alert.html",c)

	else:
		page_list = Page.objects.filter(page_name=page_name)	#page_name으로 history를 검색
		count = 0
		p = []
		for page in page_list[::-1]:
			count += 1
			p.append({"pub_date":page.pub_date,"count":count})

		c={"page":p,"page_name":page_name}
		navbar = Navbar(request)
		navbar.get_current_path()
		navbar.user_setting()
		c.update(navbar.context_dict())		
	
		return render(request,"wiki/history.html",c)

def upload_page(request,page_name=''):	#file upload 기능을 위한 method
	c = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'	#파일 업로드시 필요한 임의의 문자열을 제공하기 위한 string
	if request.method == 'POST':	#post가 있을 경우
		dummy_name =''
		is_exist = True
		while is_exist == True:	#파일 이름을 임의의 문자열로 만드는데 동일한 이름의 파일이 있을 경우 다른 랜덤한 문자열을 만듬
			dummy_name=''.join(random.sample(c,15))
			f=FilePath.objects.filter(dummy_name=dummy_name)
			if len(f) == 0 :
				is_exist = False

		UPLOAD_DIR = '/home/sle/upload'
		if 'file' in request.FILES:	#post로 받은 파일이 있을 경우 이름과 파일을 받음
			file = request.FILES['file']
			file_name = file._name

		fp = open('%s/%s' % (UPLOAD_DIR, dummy_name) , 'wb')	#파일을 저장
		for chunk in file.chunks():
			fp.write(chunk)

		fp.close()

		f = FilePath(page_name=page_name, upload_path=UPLOAD_DIR, file_name=file_name.encode('utf-8'), dummy_name=dummy_name) #파일 경로에 대한 정보를 filePath model에 저장
		f.save()

		c={'alert': '올리신 '+file_name+' 파일이 업로드 되었습니다.','location':'/sle/wiki/'+page_name}
		return render(request,"wiki/alert.html",c) #파일을 올리고 이전 페이지로 이동

	else: #파일 업로드 실패시
		c={'alert':'파일 업로드가 실패했습니다.','location':'/sle/wiki/'+page_name} 
		return render(request,"wiki/alert.html",c)


def download_page(request,page_name='',file_num=''): #파일 다운로드
	if page_name == '' or file_num == '': #파일 순서정보나 페이지 이름이 없을 경우 예외 처리
		c={'alert':'잘못된 다운로드 요청입니다.','location':'/sle/wiki/'+page_name}
		return render(request,"wiki/alert.html",c)

	file_data_list = FilePath.objects.filter(page_name=page_name) #페이지와 연결되어 있는 파일 경로 정보들을 가져온다.
	if len(file_data_list) == 0:
		c={'alert':'파일이 없습니다.','location':'/sle/wiki/'+page_name}
		return render(request,"wiki/alert.html",c)

	file_data = file_data_list[int(file_num)-1] #file_num를 통해 원하는 파일에 대한 정보를 가져온다.
	
	full_file_name = file_data.upload_path +'/'+ str(file_data.dummy_name) #다운로드 과정을 처리해준다.
	f=open(full_file_name,'rb') #파일을 읽어와서
	wrapper = FileWrapper(f) #wrap 처리해서

	response = HttpResponse(wrapper, content_type='Application/octet-stream; charset=utf-8') #response에 저장하여 보낸다.
	response['Content-Disposition'] = 'attachment; filename=' + "\""+file_data.file_name.encode("utf-8").decode('"ISO-8859-1"')+ "\""
	response['Content-Length'] = int(os.path.getsize(full_file_name))
	f.close()
	# c={'content':'attachment; filename=' + str(file_data.file_name.encode("utf-8").decode('utf-8'))}
	# return render(request,'view.html',c)
	return response
	
def delete_file(request,page_name='',file_num=''): #페이지에 첨부되어 있는 파일을 삭제하는 기능을 하는 method
	if page_name == '' or file_num == '':
		c={'alert':'잘못된 요청입니다.','location':'/sle/wiki/page/'+page_name}
		return render(request,"wiki/alert.html",c)

	file_data_list = FilePath.objects.filter(page_name=page_name)
	if len(file_data_list) == 0:
		c={'alert':'파일이 없습니다.','location':'/sle/wiki/page/'+page_name}
		return render(request,"wiki/alert.html",c)

	file_data = file_data_list[int(file_num)-1]	#삭제하기 원하는 파일의 정보를 가져와서 삭제한다.
	full_file_name = file_data.upload_path +'/'+ str(file_data.dummy_name)
	file_name = file_data.file_name
	file_data.delete()
	os.remove(full_file_name)

	c={'alert': '올리신 '+file_name+' 파일이 삭제 되었습니다.','location':'/sle/wiki/page/'+page_name}
	return render(request,"wiki/alert.html",c)

def instagram_example(request):
	# access_token = "YOUR_ACCESS_TOKEN"
	# api = InstagramAPI(access_token="551091148.1118900.39c04ca10ec649a78f80d2bde2cb4aa1")
	# recent_media, next_ = api.user_recent_media(user_id="hongdan009",count=10)
	# c=[]
	# for media in recent_media:
	# 	c.append(media.caption.text)

	# s = '\n'.join(c)
	# s=""
	api = InstagramAPI(client_id='1118900683bb413993f5e374ac9ea021', client_secret='d20ea751a7be44adb41ac19d3ad6b42c')
	# suzy= api.user(user_id="1507979106")
	# recent_media = suzy.user_media_feed()
	recent_media, next_ = api.user_recent_media(user_id="1507979106",count=50)
	while next_:
		more_media, next_ = api.user_recent_media(with_next_url=next_)
		recent_media.extend(more_media)	

	# for media in recent_media:
	# 	s += '<img src="'+media.images["thumbnail"].url+'">'

	s = []
	numPerPage = 8

	for media in recent_media :
		s += [media.images['standard_resolution'].url]

	# return HttpResponse(s)
	c = {'photo':s[:numPerPage]}
	return render(request,"wiki/insta.html",c)

def instagram_page(request) :
	curPage = request.GET['currentPage']
	numPerPage = 8

	api = InstagramAPI(client_id='1118900683bb413993f5e374ac9ea021', client_secret='d20ea751a7be44adb41ac19d3ad6b42c')
	recent_media, next_ = api.user_recent_media(user_id="1507979106",count=50)
	while next_:
		more_media, next_ = api.user_recent_media(with_next_url=next_)
		recent_media.extend(more_media)

	s = []

	for media in recent_media :
		s += [media.images['standard_resolution'].url]

	s = s[(curPage-1)*numPerPage:curPage*numPerPage]
	c = {'photo':s}
	return render(request,"wiki/insta.html",c)