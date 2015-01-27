from django.conf.urls import patterns, include, url
from wiki import views

urlpatterns = patterns('',
    url(r'^$', views.view_page),
    url(r'^instagram/$', views.instagram_example),
    url(r'^search/$', views.search_page),
    url(r'^page/(?P<page_name>[^/]+)/$', views.view_page),
    url(r'^edit/(?P<page_name>[^/]+)/(?P<section>[^/]+)/$', views.edit_page),
    url(r'^save/(?P<page_name>[^/]+)/(?P<section>[^/]+)/$', views.save_page),
    url(r'^history/(?P<page_name>[^/]+)/$', views.history_page),
    url(r'^upload/(?P<page_name>[^/]+)/$', views.upload_page),
    url(r'^download/(?P<page_name>[^/]+)/(?P<file_num>[^/]+)/$', views.download_page),
    url(r'^delete/(?P<page_name>[^/]+)/(?P<file_num>[^/]+)/$', views.delete_file),
    url(r'^page/(?P<page_name>[^/]+)/(?P<page_num>[^/]+)/$', views.view_page),
)