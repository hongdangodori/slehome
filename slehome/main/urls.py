from django.conf.urls import patterns, include, url

from main import views

urlpatterns = patterns('',
    url(r'^$', views.main_index),
    url(r'^register/$', views.register_index),
    url(r'^register/(?P<stu_num>[^/]+)/$', views.register_real),
)
