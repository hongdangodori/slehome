from django.conf.urls import patterns, include, url
from wiki import views

urlpatterns = patterns('',
    url(r'^$', views.view_page),
    url(r'^search/$', views.search_page),
    url(r'^(?P<page_name>[^/]+)/$', views.view_page),
    url(r'^(?P<page_name>[^/]+)/edit/$', views.edit_page),
    url(r'^(?P<page_name>[^/]+)/save/$', views.save_page),
    url(r'^(?P<page_name>[^/]+)/history/$', views.history_page),
    url(r'^(?P<page_name>[^/]+)/upload/$', views.upload_page),
    url(r'^(?P<page_name>[^/]+)/download/(?P<file_num>[^/]+)/$', views.download_page),
    url(r'^(?P<page_name>[^/]+)/delete/(?P<file_num>[^/]+)/$', views.delete_file),
    url(r'^(?P<page_name>[^/]+)/(?P<page_num>[^/]+)/$', views.view_page),
)