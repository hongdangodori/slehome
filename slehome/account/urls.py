from django.conf.urls import patterns, include, url

from account import views

urlpatterns = patterns('',
    url(r'^register/$', views.register_index),
    url(r'^register/(?P<stu_num>[^/]+)/$', views.register_real),
    url(r'^account/$', views.account_index),
    url(r'^account/account_settings/$', views.account_settings),
    url(r'^account/change_password/$', views.change_password),
    url(r'^account/edit_introduction/$', views.edit_introduction),
    url(r'^account/edit_introduction/save_intro/$', views.save_intro),
    url(r'^account/edit_introduction/save_stat/$', views.save_stat),
)