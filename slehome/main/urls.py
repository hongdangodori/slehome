from django.conf.urls import patterns, include, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.main_index),
    url(r'^register/$', views.register_one),
    #url(r'^register/(?P<username>[-\w]+)/$', views.register_two),
)