from django.conf.urls import patterns, url

from infoboards import views

urlpatterns = patterns('',
	url(r'^$', views.ellip_test), 
	url(r'^test2/$', views.test2),
	url(r'^test2/(?P<name>\w+)/$', views.test2),
)