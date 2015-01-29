#-*- coding:utf-8 -*-
from django.shortcuts import render

from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist

from freeboards.models import FreeBoard, LikeArticle
from freeboards.pagingHelper import pagingHelper

from django.contrib.auth.decorators import login_required
from navbar.shared import NavbarForMembers

rowsPerPage = 10

@login_required
def home(request):

	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	boardList = FreeBoard.objects.order_by('-id')[:rowsPerPage]
	currentPage = 1

	totalCnt = FreeBoard.objects.all().count()

	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)	

	context = {'boardList': boardList,
		'totalCnt': totalCnt,
		'currentPage': currentPage,
		'totalPageList': totalPageList
		}

	######################
	context.update(navbar.context_dict())
	#######################

	return render(request, "freeboards/listSpecificDropdown.html", context)


def showWriteForm(request):
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	context = { 'name': request.user.myuser.nickname }
	######################
	context.update(navbar.context_dict())
	#######################
	return render(request, 'freeboards/writeBoard.html', context)


@csrf_exempt
def doWriteBoard(request):

	br = FreeBoard(user = request.user.myuser.nickname,
		category = request.POST['category'],
		title = request.POST['title'],
		contents = request.POST['contents'],
		pub_date = timezone.now(),
		hits = 0
		)
	br.save()

	return HttpResponseRedirect("/sle/freeboards/listSpecificPageWork?currentPage=1")


def listSpecificPageWork(request):
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	currentPage = request.GET['currentPage']
	totalCnt = FreeBoard.objects.all().count()
	boardList = FreeBoard.objects.order_by('-id')[int(rowsPerPage)*(int(currentPage)-1) : int(rowsPerPage)*int(currentPage)]

	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)

	context = {'boardList': boardList,
		'totalCnt': totalCnt,
		'currentPage': int(currentPage),
		'totalPageList': totalPageList
		}

	context.update(navbar.context_dict())

	return render(request, 'freeboards/listSpecificPage.html', context)


def viewWork(request):
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################


	pk = request.GET['writing_id']
	boardData = FreeBoard.objects.get(id=pk)
	likeCnt = LikeArticle.objects.filter(article_id = pk).count()
	
	# hit++
	FreeBoard.objects.filter(id=pk).update(hits = boardData.hits + 1)
	boardData = FreeBoard.objects.get(id=pk)

	context = {
			'writing_id' : request.GET['writing_id'],
			'currentPage': request.GET['currentPage'],
			'searchStr' : request.GET['searchStr'],
			'boardData' : boardData,
			'likeCnt' : likeCnt,
			'likeData' : ''
		}

	try:
			likeData = LikeArticle.objects.get(user=request.user.myuser.nickname, article_id=pk)
			context.update({'likeData' : likeData})

	except ObjectDoesNotExist:
			pass

	context.update(navbar.context_dict())

	return render(request, 'freeboards/viewMemo.html', context)
	

def listSpecificPageUpdate(request):
	#######################
	navbar = NavbarForMembers(request)
	navbar.get_current_path()
	navbar.user_setting()

	if request.method == "POST":
		if 'logout' in request.POST:
			navbar.user_logout()
	########################

	writing_id = request.GET['writing_id']
	currentPage = request.GET['currentPage']
	searchStr = request.GET['searchStr']
	boardData = FreeBoard.objects.get(id=writing_id)

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
	#######################
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
	FreeBoard.objects.filter(id=writing_id).update(
		category = request.POST['category'],
		title = request.POST['title'],
		contents = request.POST['contents'],
		)

	context.update(navbar.context_dict())

	url = '/sle/freeboards/listSpecificPageWork?currentPage=' + currentPage
	return HttpResponseRedirect(url)


def deleteSpecificRow(request):
	pk = request.GET['writing_id']
	currentPage = request.GET['currentPage']

	p = FreeBoard.objects.get(id=pk)
	p.delete()

	# if last memo deleted, page--
	totalCnt = FreeBoard.objects.all().count()
	pagingHelperIns = pagingHelper()

	totalPageList = pagingHelperIns.getTotalPageList( totalCnt, rowsPerPage)
	if( int(currentPage) in totalPageList):
		currentPage=currentPage
	else:
		currentPage= int(currentPage)-1

	url = '/sle/freeboards/listSpecificPageWork?currentPage=' + str(currentPage)
	return HttpResponseRedirect(url)


def listSearchedSpecificPage(request):
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

	boardList = FreeBoard.objects.filter(title__contains=searchStr)
	totalCnt  = FreeBoard.objects.filter(title__contains=searchStr).count()

	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)

	context = {
		'boardList': boardList,
		'totalCnt': totalCnt,
		'pageForView': int(pageForView),
		'searchStr': searchStr,
		'totalPageList': totalPageList,
	}

	context.update(navbar.context_dict())

	return render(request, 'freeboards/listSearchedSpecificPage.html', context)


@csrf_exempt
def searchWithSubject(request):
	searchStr = request.POST['searchStr']

	url = '/sle/freeboards/listSearchedSpecificPage?searchStr='+searchStr+'&pageForView=1'
	return HttpResponseRedirect(url)


@login_required
def pushLike(request):
	pk = request.GET['writing_id']
	currentPage = request.GET['currentPage']
	try:
		la = LikeArticle.objects.get(user=request.user.myuser.nickname, article=pk)
		if(la.is_like()):
			la.delete()
		else:
			la.like = True
			la.save()


	except ObjectDoesNotExist:
		la = LikeArticle(user = request.user.myuser.nickname,
				article = FreeBoard.objects.get(id=pk),
				like = True,
			)
		la.save()

	url = '/sle/freeboards/viewWork?writing_id='+str(pk)+'&currentPage='+str(currentPage)+'&searchStr=None'
	return HttpResponseRedirect(url)
