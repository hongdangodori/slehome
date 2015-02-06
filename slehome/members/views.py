from django.shortcuts import render, render_to_response, redirect
from django.http import *
from django.contrib import auth
from django.core.context_processors import csrf
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required
from navbar.shared import NavbarForMembers
from account.models import MemberIntro, PhotoLink, Stat
from django.http import HttpResponse
from django.contrib.auth.models import User
import simplejson


@login_required
def members_index(request,page_number='1',sort_type='1'):	#member 소개 페이지를 위한 method이다.

	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()	#navbar를 채우기 위한 과정
	member_list=[]
	if sort_type == '1':
		member_intro_set=MemberIntro.objects.all().order_by('user__myuser__stu_num') #member 소개 정보를 다 가져온다.\
	elif sort_type == '2':
		member_intro_set=MemberIntro.objects.all().order_by('-user__myuser__level') #member 소개 정보를 다 가져온다.\
	else:
		member_intro_set=MemberIntro.objects.all().order_by('user__myuser__stu_num') #member 소개 정보를 다 가져온다.\

	member_sort_list=[]
	member_sort_list.append({"num":'1',"value":'학번순'})
	member_sort_list.append({"num":'2',"value":'레벨순'})	
	##########################################################
	page_number = int(page_number)
	member_page = 9	# 한 페이지당 보이는 사진 수
	total_members=len(member_intro_set)
	total_page=(total_members + (member_page-1))//member_page
	prev_page = (page_number - 1) // 10 * 10			# 이전 페이지 구하기
	next_page = (page_number - 1) // 10 * 10 + 11		# 다음 페이지 구하기
	page_list= [page+1 for page in range(prev_page, (next_page < total_page and next_page-1) or total_page)]
	##########################################################
	member_intro_set = member_intro_set[(page_number-1)*member_page : page_number*member_page]
	for member_intro in member_intro_set: #member intro 정보 순서대로 작업을 한다.		
		try:
			photo_link=member_intro.photolink #member intro와 연결된 사진 정보를 가져온다.
		except:
			photo_link="6.png"
		
		name=member_intro.user.username #member의 이름 정보를 가져온다.		
		
		count = 0
		member_list.append({"name":name,"photo_link":photo_link}) #template에서 쓸 정보를 세팅한다.

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()

	context_dict = {"member_list":member_list,"page_list":page_list,"page_number":page_number, 'total_page':total_page, 'prev_page':prev_page, 'next_page':next_page,'sort_type':sort_type,'member_sort_list':member_sort_list}
	context_dict.update(navbar.context_dict())	#template에서 쓸 정보를 싸놓는다.

	return render(request,"members/members_index.html",context_dict)	#보낸다.

def mk_member_modal(request):
	user_name=request.POST['username']
	if user_name == "":
		user_name="hongdan"
	try:
		member_intro = User.objects.get(username=user_name).memberintro
		bar_type_list=["warning","danger","success","info"]	#stat 게이지 바 색깔을 위한 정보이다.
		stat_list=[]
		stats = member_intro.stat_set.all() #member intro와 연결된 stat 정보를 가져온다.
		count = 0
		try:
			photo_link=member_intro.photolink.upload_path+member_intro.photolink.file_name #member intro와 연결된 사진 정보를 가져온다.
		except:
			photo_link=""

		for stat in stats:
			stat_list.append({"stat_name":stat.stat_name,"stat_value":stat.stat_value,"bar_type":bar_type_list[count]})
			count += 1
		birthday=member_intro.user.myuser.birthday
		front_birth=''
		if int(birthday[:2]) > 60:
			front_birth='19'
		else:
			front_birth='20'			
	
		birthday= front_birth+birthday[:2]+" 년 "+birthday[2:4]+" 월 "+birthday[4:6]+" 일" 

		data={"photo_link":photo_link,"name":member_intro.user.myuser.fullname,"phone_num":member_intro.user.myuser.phone_num,"birthday":birthday,"member_intro":member_intro.intro,'stat_list':stat_list,'level':member_intro.user.myuser.level,'point':member_intro.user.myuser.point,"alert":""}		
		# data={"name":member_intro.user.myuser.fullname,'stat_list':stat_list,"alert":""}		
	except Exception as e:
		data={"alert":str(e)}
	
	return HttpResponse(simplejson.dumps(data))