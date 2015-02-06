from django.conf.urls import patterns, include, url
from imagecrop import views

urlpatterns = patterns('',
    url(r'^test/$', views.test_jcrop),
    url(r'^del_photo/$', views.del_photo),
    url(r'^$', views.upload_profile_image),
)