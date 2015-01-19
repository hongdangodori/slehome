from django.conf.urls import patterns, url

from freeboards import views

urlpatterns = patterns('',
	url(r'^$', views.home), 
	url(r'^showWriteForm/$', views.showWriteForm), 
	url(r'^doWriteBoard/$', views.doWriteBoard),
	url(r'^listSpecificPageWork/$', views.listSpecificPageWork),
	url(r'^listSpecificPageWork/(?P<currentPage>\d+)/currentPage/$', views.listSpecificPageWork), #, name='listSpecificPageWork'),
	url(r'^viewWork/(?P<writing_id>\d+)/$', views.viewWork)
)
