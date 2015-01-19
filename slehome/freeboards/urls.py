from django.conf.urls import patterns, url

from freeboards import views

urlpatterns = patterns('',
	url(r'^$', views.home), #, name='index'),
	url(r'^showWriteForm/$', views.showWriteForm), #, name='showWriteForm'),
	url(r'^doWriteBoard/$', views.doWriteBoard), #, name='doWriteBoard'),	
	url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
	url(r'^listSpecificPageWork/(?P<currentPage>\d+)/currentPage/$', views.listSpecificPageWork), #, name='listSpecificPageWork'),
	url(r'^viewWork/(?P<memo_id>)\d+)/$', views.viewWork)
)
