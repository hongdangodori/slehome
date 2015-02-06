#-*- coding:utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
import simplejson
from django.core import serializers

from account.models import MyUser
from django.contrib.auth.models import User
from freeboards.models import FreeBoards, LikeArticles, ArticleComments, LikeComments
from freeboards.pagingHelper import pagingHelper

from django.contrib.auth.decorators import login_required
from navbar.shared import NavbarForMembers

# 게시물 한 페이지에 몇 개의 게시글이 보일지 결정하는 변수
rowsPerPage = 10


@login_required
def home(request):
	"""
		자유게시판 첫 페이지
	"""

	####################### navbar 목록 및 로그인 정보 가져오기
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	
	boardList = FreeBoards.objects.order_by('-id')[:rowsPerPage] # 최신글부터 정렬하여 list에 가져온다.
	currentPage = 1 # 처음 보여지는 페이지는 1 page

	totalCnt = FreeBoards.objects.all().count() # 총 게시물 수

	# pagingHelper object를 만들어서 pagelist를 받아온다.
	pagingHelperIns = pagingHelper() 
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)	

	# 넘겨줄 dict data.
	context = {'boardList': boardList,
		'totalCnt': totalCnt,
		'currentPage': currentPage,
		'totalPageList': totalPageList
		}

	######################
	context.update(navbar.context_dict()) # navbar 정보 추가
	#######################

	return render(request, "freeboards/listSpecificPage.html", context)


def showWriteForm(request):
	"""
		게시판 페이지에서 'write' 버튼을 클릭하면 이 함수를 거쳐 writeBoard html로 넘어간다.
	"""

	####################### navbar 목록 및 로그인 정보 가져오기
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	user_nickname = User.objects.get(username = request.user.username)
	context = {'user_nickname': user_nickname,}
	######################
	context.update(navbar.context_dict())
	#######################
	return render(request, 'freeboards/writeBoard.html', context)


@csrf_exempt
def doWriteBoard(request):
	"""
		writeBoard 에서 'submit' 버튼을 누르면 row 생성해서 insert table.
	"""

	br = FreeBoards(
		user = User.objects.get(username=request.user.username),
		category = request.POST['category'],
		title = request.POST['title'],
		contents = request.POST['contents'],
		pub_date = timezone.now(),
		hits = 0
		)
	br.save()

	# 1page로 redirect.
	return HttpResponseRedirect("/sle/freeboards/listSpecificPageWork?currentPage=1")


def listSpecificPageWork(request):
	"""
		page list에서 특정 페이지를 클릭했을 때 보여주는 view를 처리한다.
	"""

	####################### navbar 목록 및 로그인 정보 가져오기
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	currentPage = request.GET['currentPage']	# 클릭한 page 정보를 받아온다.
	totalCnt = FreeBoards.objects.all().count()	# 총 게시물 수

	# 받아온 page에 표시할 게시물을 역순으로 가져온다.
	# ex) 총 게시물 10개, rowsPerPage 4개일 때, 2 페이지는 역순으로 4(4*1)~7(4*2)번째 게시물이다. (index: 0~)
	boardList = FreeBoards.objects.order_by('-id')[int(rowsPerPage)*(int(currentPage)-1) : int(rowsPerPage)*int(currentPage)]

	# pagingHelper object를 만들어서 pagelist를 받아온다.
	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)

	# 넘겨줄 dict data.
	context = {'boardList': boardList,
		'totalCnt': totalCnt,
		'currentPage': int(currentPage),
		'totalPageList': totalPageList
		}

	context.update(navbar.context_dict())

	return render(request, 'freeboards/listSpecificPage.html', context)


def viewWork(request):
	"""
		특정 게시물을 클릭했을 때 게시물을 보여주기 위한 view를 처리한다.
	"""

	####################### navbar 목록 및 로그인 정보 가져오기
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################


	pk = request.GET.get('writing_id', 1)		# 게시물 번호
	boardData = FreeBoards.objects.get(id=pk)	# 해당 게시물을 DB에서 가져온다.
	likeCnt = LikeArticles.objects.filter(article_id = pk).count()	# 해당 게시물의 좋아요 개수를 DB에서 가져온다.
	
	# hit++ 
	FreeBoards.objects.filter(id=pk).update(hits = boardData.hits + 1)
	boardData = FreeBoards.objects.get(id=pk) # hit++ 된 상태를 다시 가져와야 view에 hit++이 적용되어 보여짐

	# 유저가 게시물을 이전에 like 했었는지 찾는다. 이 정보를 가지고 template에서 like 버튼의 색깔을 결정한다. 
	try:
			likeData = LikeArticles.objects.get(user=User.objects.get(username=request.user.username), article_id=pk)

	except ObjectDoesNotExist:
			likeData = ''

	# 게시물에 댓글이 달려있는지 확인한다. 없다면 빈 공백을 표시한다.
	try:
			commentList = ArticleComments.objects.filter(article=pk)

	except ObjectDoesNotExist:
			commentList = ''


	currentUser = User.objects.get(username=request.user.username)
	# 넘겨줄 dict data.
	context = {
			'writing_id' : pk,
			'currentUser' : currentUser,
			'currentPage': request.GET.get('currentPage', 1),
			'searchStr' : request.GET.get('searchStr', None),
			'boardData' : boardData,
			'likeCnt' : likeCnt,
			'likeData' : likeData,
			'commentList' : commentList,
		}
	context.update(navbar.context_dict())

	return render(request, 'freeboards/viewMemo.html', context)
	

def listSpecificPageUpdate(request):
	"""
		게시물의 Edit버튼을 클릭했을 경우 처리해주는 view.
	"""
	####################### navbar 목록 및 로그인 정보 가져오기
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	# 게시물 번호, 현재 page와 검색어(없었다면 none), 게시물 Data를 가져온다.
	writing_id = request.GET['writing_id']
	currentPage = request.GET['currentPage']
	searchStr = request.GET['searchStr']
	boardData = FreeBoards.objects.get(id=writing_id)

	# 넘겨줄 dict data.
	context = {
		'writing_id': writing_id,
		'currentPage': currentPage,
		'searchStr': searchStr,
		'boardData': boardData,
	}

	context.update(navbar.context_dict())

	return render(request, 'freeboards/viewForUpdate.html', context)


@csrf_exempt
def updateBoard(request):
	"""
		게시물 Edit에서 'confirm'을 클릭하면 DB 내용을 업데이트한다.
	"""
	####################### navbar 목록 및 로그인 정보 가져오기
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	writing_id = request.POST['writing_id']
	currentPage = request.POST['currentPage']
	searchStr = request.POST['searchStr']

	context = {}

	# update Database
	FreeBoards.objects.filter(id=writing_id).update(
		category = request.POST['category'],
		title = request.POST['title'],
		contents = request.POST['contents'],
		)

	context.update(navbar.context_dict())

	url = '/sle/freeboards/listSpecificPageWork?currentPage=' + currentPage
	return HttpResponseRedirect(url)


def deleteSpecificRow(request):
	"""
		게시물 삭제를 처리해주는 view.
	"""
	pk = request.GET['writing_id']
	currentPage = request.GET['currentPage']

	# 해당 게시물을 찾아서 DB에서 삭제한다. 관련 data모두 삭제.
	p = FreeBoards.objects.get(id=pk)
	pChildLA = LikeArticles.objects.filter(article=pk)
	pChildAC = ArticleComments.objects.filter(article=pk)
	for rows in pChildAC:
		ACChildLC = LikeComments.objects.filter(comments=rows.comments)
		ACChildLC.delete()
	pChildAC.delete()
	pChildLA.delete()
	p.delete()


	# 만약 삭제한 게시물이 마지막 페이지의 마지막 게시물이라면, 해당 페이지를 삭제한다.
	totalCnt = FreeBoards.objects.all().count()
	pagingHelperIns = pagingHelper()

	totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
	if( int(currentPage) in totalPageList):
		currentPage=currentPage
	else:
		currentPage= int(currentPage)-1

	url = '/sle/freeboards/listSpecificPageWork?currentPage=' + str(currentPage)
	return HttpResponseRedirect(url)


@csrf_exempt
def searchWithSubject(request):
	"""
		게시물 검색을 하면 검색어를 가져와 밑의 'listSearchedSpecificPage'로 정보를 보내준다.
		'listSearchedSpecificPage'에서 검색어로 검색된 새로운 page list를 생성한다.
	"""
	searchStr = request.POST['searchStr']

	url = '/sle/freeboards/listSearchedSpecificPage?searchStr='+searchStr+'&pageForView=1'
	return HttpResponseRedirect(url)


def listSearchedSpecificPage(request):
	"""
		게시물을 검색할 때 처리해주는 page list view. 게시물의 제목만 검색한다.
	"""
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	searchStr = request.GET['searchStr']
	pageForView = request.GET['pageForView']

	# 게시물의 제목에서 검색어를 포함하는 게시물과 그 개수를 가져온다.
	boardList = FreeBoards.objects.filter(title__contains=searchStr)
	totalCnt  = FreeBoards.objects.filter(title__contains=searchStr).count()

	# 검색된 게시물들을 가지고 새로 page list를 만든다.
	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)

	# 넘겨줄 dict data.
	context = {
		'boardList': boardList,
		'totalCnt': totalCnt,
		'pageForView': int(pageForView),
		'searchStr': searchStr,
		'totalPageList': totalPageList,
	}

	context.update(navbar.context_dict())

	return render(request, 'freeboards/listSearchedSpecificPage.html', context)


@login_required
def pushLike(request):
	"""
		게시물에서 like 버튼을 누르면 처리해주는 view.
		ajax가 이 함수를 call한다. 
	"""

	pk = request.GET['writing_id']

	# 유저가 해당 게시물을 좋아하는 상태인지 확인하여
	# like한 적이 있는 경우 - like를 취소한다는 뜻이므로 like DB에서 삭제한다.
	# like한 적이 없는 경우 - 유저가 해당 게시물을 좋아한다는 정보를 DB에 추가한다
	try:
		# 해당 게시물을 like하고 있는 경우
		la = LikeArticles.objects.get(user = User.objects.get(username=request.user.username), article=pk)
		if(la.is_like()):
			la.delete()
			likeCnt = LikeArticles.objects.filter(article=pk).count()
			FreeBoards.objects.filter(id=pk).update(like = likeCnt)
		else: # Never happens (like object가 없다면 except로 넘어가기 때문)
			la.like = True
			la.save()
			likeCnt = LikeArticles.objects.filter(article=pk).count()
			FreeBoards.objects.filter(id=pk).update(like = likeCnt)

	# 해당 게시물을 like하지 않고 있는 경우
	except ObjectDoesNotExist:
		la = LikeArticles(
				user = User.objects.get(username=request.user.username),
				article = FreeBoards.objects.get(id=pk),
				like = True,
			)
		la.save()
		likeCnt = LikeArticles.objects.filter(article=pk).count()
		FreeBoards.objects.filter(id=pk).update(like = likeCnt)

	# like버튼의 count를 보내준다. 
	if likeCnt == 0:
		dLike = 'like'
	elif likeCnt == 1:
		dLike = str(likeCnt)+'like'
	else:	
		dLike = str(likeCnt)+'likes'

	data = {
		'dLike': dLike,
	}
	return HttpResponse(simplejson.dumps(data), content_type="application/json")
	# return HttpResponse(data)


@login_required
@csrf_exempt
def pushComment(request):
	"""
		게시물에 댓글이 달리면 처리해주는 view.
		ajax가 이 함수를 call한다.
		미완성
	"""

	pk = request.POST.get('writing_id', 1)

	# if(게시물 댓글):
	ac = ArticleComments(
		user = User.objects.get(username=request.user.username),
		article = FreeBoards.objects.get(id=pk),
		comments = request.POST.get('comments', 'Nothing'),
		target = 0,
		pub_date = timezone.now(),
		like = 0,
		)
	ac.save()

	comCnt = ArticleComments.objects.filter(article=pk).count()
	user = MyUser.objects.get(nickname=request.user.myuser)
	data = {
		'writing_id': pk,
		'user': user.nickname,
		'comments': ac.comments,
		'target': ac.target,
		'pub_date': str(ac.pub_date),
		'like': ac.like,
		'comCnt': comCnt,
	}
	
	return HttpResponse(simplejson.dumps(data), content_type="application/json")
	# url = 'freeboards/comments.html'
	# return render(request, url, data)

