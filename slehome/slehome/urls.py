from django.conf.urls import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sle/$', 'sitesle.views.home', name='home'),
    url(r'^sle/freeboards/', include('freeboards.urls'), name="freeboards"),
    url(r'^sle/wiki/', include('wiki.urls'), name="wiki"),
)