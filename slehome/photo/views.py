from django.shortcuts import render	#template로 넘어가는데 사용되는 메소드
from django.core.context_processors import csrf	#form을 통해 data를 넘겨받을때 사용해야 하는 것
from django.http import HttpResponseRedirect, HttpResponse #HttpResponse를 위해 사용
from django.db.models import Q 	#django의 model에서 필요한 자료를 뽑아낼 때 사용됨 or나 and가 가능하게 해주는 기능


from navbar.shared import Navbar
from instagram.client import InstagramAPI # instagram을 사용하기 위한 module 차후에 옮길 예정
# Create your views here.

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
	navbar = Navbar(request)
	navbar.get_current_path()
	navbar.user_setting()
	c.update(navbar.context_dict())		
	return render(request,"photo/insta.html",c)

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
	return render(request,"photo/insta.html",c)