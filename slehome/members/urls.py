from django.conf.urls import patterns, url

from members import views

urlpatterns = patterns('',
	url(r'^$', views.members_index),
	url(r'^mk_modal/$', views.mk_member_modal),
	url(r'^(?P<page_number>[^/]+)/$', views.members_index),
	url(r'^(?P<page_number>[^/]+)/(?P<sort_type>[^/]+)/$', views.members_index),
)
