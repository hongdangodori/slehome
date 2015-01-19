from django.shortcuts import render

# Create your views here.
#-*- coding:utf-8 -*-
from django.shortcuts import render_to_response
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect

from freeboards.models import DjangoBoard
from freeboards.pagingHelper import pagingHelper

rowsPerPage = 2

def home(request):
	boardList = DjangoBoard.objects.order_by('-id')[0:2]
	currentPage = 1

	totalCnt = DjangoBoard.objects.all().count()

	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)	
	print('totalPageList')

	return render_to_response("listSpecificPage.html", {'boardList': boardList,	
		'totalCnt': totalCnt, 'currentPage': currentPage, 'totalPageList': totalPageList})


def showWriteForm(request):
	return render_to_response('writeBoard.html')


@csrf_exempt
def doWriteBoard(request):
	br = DjangoBoard(subject = request.POST['subject'],
		name = request.POST['name'],
		mail = request.POST['email'],
		memo = request.POST['memo'],
		created_date = timezone.now(),
		hits = 0
		)
	br.save()

	# url = '/listSpecificPageWork?currentPage=1'
	return HttpResponseRedirect("/freeboards/")


def listSpecificPageWork(request):
	currentPage = request.GET['currentPage']
	totalCnt = DjangoBoard.objects.all().count()

	print('currentPage =', currentPage)

	pagingHelperIns = pagingHelper()
	totalPageList = pagingHelperIns.getTotalPageList(totalCnt, rowsPerPage)

	print('totalPageList', totalPageList)

	# pages of currentPage
	f = rowsPerPage * currentPage
	b = f - rowsPerPage + 1
	boardList = DjangoBoard.objects.raw('SELECT * FROM freeboards_djangoboard WHERE id between %s and %s', [b, f])
	# boardList = DjangoBoard.objects.raw('SELECT Z.*	FROM(SELECT X.*, ceil(rownum / %s) as page FROM (SELECT ID, SUBJECT, NAME, CREATED_DATE, MAIL, MEMO, HITS FROM FREEBOARDS ORDER BY ID DESC) X) Z WHERE page = %s', [rowsPerPage, currentPage])


	return render_to_response('listSpecificPage.html', {'boardList': boardList, 'totalCnt': totalCnt,
		'currentPage': currentPage, 'totalPageList': totalPageList})


def viewWork(request):
	pk = request.GET['memo_id']
	boardData = DjangoBoard.objects.get(id=pk)

	# hit++
	DjangoBoard.objects.filter(id=pk).update(hits = boardData.hits + 1)

	return render_to_response('viewMemo.html', {'memo_id': request.GET['memo_id'],
		'currentPage': request.GET['currentPage'],
		'searchStr': request.GET['searchStr'],
		'boardData': boardData
		})
	