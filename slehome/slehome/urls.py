from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'MyProject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^sle/$', 'sitesle.views.home', name='home'),
    url(r'^sle/freeboards/', include('freeboards.urls'), name="freeboards"),
    url(r'^sle/wiki/$', 'wiki.views.view_page'),
    url(r'^sle/wiki/search/$', 'wiki.views.search_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/$', 'wiki.views.view_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/edit/$', 'wiki.views.edit_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/save/$', 'wiki.views.save_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/history/$', 'wiki.views.history_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/upload/$', 'wiki.views.upload_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/download/(?P<file_num>[^/]+)/$', 'wiki.views.download_page'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/delete/(?P<file_num>[^/]+)/$', 'wiki.views.delete_file'),
    url(r'^sle/wiki/(?P<page_name>[^/]+)/(?P<page_num>[^/]+)/$', 'wiki.views.view_page'),

    # url(r'^sle/wiki/alert/$', 'wiki.views.alert_page'),
)