from django.conf.urls import patterns, include, url
from photo import views

urlpatterns = patterns('',
    url(r'^$', views.instagram_example),
)