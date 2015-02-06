from django.shortcuts import render	#template로 넘어가는데 사용되는 메소드
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist

import simplejson

from datetime import datetime

from navbar.shared import Navbar

from account.models import MyUser

from photo.models import Photos, PhotoComments
from photo.getPhotos import Instagram

def instagram_page(request, page_number='1') :
	page_number = int(page_number)
	photo_page = 8		# 한 페이지당 보이는 사진 수

	photo = Instagram.getData()
	total_photos = len(photo)		# 총 사진 수
	total_page = (total_photos + (photo_page - 1)) // photo_page		# 총 페이지 수

	# 페이지 예외 처리
	if page_number < 1 :
		page_number = 1
	elif page_number > total_page :
		page_number = total_page

	photo = photo[(page_number-1)*photo_page : page_number*photo_page]		# 페이지에 보여질 사진들

	prev_page = (page_number - 1) // 10 * 10			# 이전 페이지 구하기
	next_page = (page_number - 1) // 10 * 10 + 11		# 다음 페이지 구하기


	page_list = [page+1 for page in range(prev_page, (next_page < total_page and next_page-1) or total_page)]		# 페이지 수들

	c = {'photo':photo, 'page_list':page_list, 'page_number':page_number, 'total_page':total_page, 'prev_page':prev_page, 'next_page':next_page}

	###########################################
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()
	c.update(navbar.context_dict())
	###########################################

	return render(request,"photo/insta.html",c)

@login_required
@csrf_exempt
def comment_push(request) :
	link = request.POST.get('photo')
	try :
		pk = Photos.objects.get(link=link)
	except ObjectDoesNotExist :
		data = {'alert' : 'no photos'}
		return HttpResponse(simplejson.dumps(data), content_type="application/json")

	try :
		u = User.objects.get(username=request.user.username)
	except ObjectDoesNotExist :
		data = {'alert' : 'no user'}
		return HttpResponse(simplejson.dumps(data), content_type="application/json")

	com = PhotoComments(
		user = u,
		photo = pk,
		comments = request.POST.get('comments', 'Nothing'),
		pub_date = datetime.now()
		)
	com.save()

	try :
		user = MyUser.objects.get(nickname=str(request.user.myuser))
	except ObjectDoesNotExist :
		data = {'alert' : 'no user nickname'}
		return HttpResponse(simplejson.dumps(data), content_type="application/json")

	data = {
		'user' : user.nickname,
		'comments' : com.comments,
		'pub_date' : str(com.pub_date.strftime('%Y-%m-%d')),
		'alert' : ''
	}

	return HttpResponse(simplejson.dumps(data), content_type="application/json")

@csrf_exempt
def comment_show(request) :
	link = request.POST.get('photo')

	try :
		pk = Photos.objects.get(link=link)
	except ObjectDoesNotExist :
		data = {'alert' : 'no photos'}
		return HttpResponse(simplejson.dumps(data), content_type="application/json")

	com = PhotoComments.objects.filter(photo=pk).order_by('pub_date')

	if len(com) > 0 :
		user, comments, pub_date = [], [], []
		for c in com :
			try :
				u = User.objects.get(username=str(c.user))
			except ObjectDoesNotExist :
				data = {'alert' : 'no user'}
				return HttpResponse(simplejson.dumps(data), content_type="application/json")

			user += [u.myuser.nickname]
			comments += [c.comments]
			pub_date += [str(c.pub_date)]
		data = {
			'user' : user,
			'comments' : comments,
			'pub_date' : pub_date,
			'alert' : ''
		}
	else :
		data = {
			'comments' : '',
			'alert' : ''
		}

	return HttpResponse(simplejson.dumps(data), content_type="application/json")