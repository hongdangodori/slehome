from django.conf.urls import patterns, include, url
from photo import views

urlpatterns = patterns('',
    url(r'^$', views.instagram_page),
    url(r'^comment/push/$', views.comment_push),
    url(r'^comment/show/$', views.comment_show),
    url(r'^(?P<page_number>[^/]+)/$', views.instagram_page),
)