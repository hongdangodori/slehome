from django.conf.urls import patterns, url

from freeboards import views

urlpatterns = patterns('',
	url(r'^$', views.home), 
	url(r'^showWriteForm/$', views.showWriteForm), 
	url(r'^doWriteBoard/$', views.doWriteBoard),
	url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
	url(r'^listSpecificPageWork/(?P<currentPage>\d+)/currentPage/$', views.listSpecificPageWork), #, name='listSpecificPageWork'),
	url(r'^viewWork/$', views.viewWork),
	# url(r'^searchWithSubject/$', views),
	url(r'^listSearchedSpecificPageWork/$', views.listSearchSpecificPageWork),
	url(r'^listSpecificPageUpdate/$', views.listSpecificPageUpdate),
	url(r'^updateBoard/$', views.updateBoard),
	url(r'^deleteSpecificRow/$', views.deleteSpecificRow),
)
