from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^sle/', include('main.urls'), name="main"),
    url(r'^sle/freeboards/', include('freeboards.urls'), name="freeboards"),
    url(r'^sle/wiki/', include('wiki.urls'), name="wiki"),
    url(r'^sle/members/', include('members.urls'), name="members"),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root': settings.MEDIA_ROOT}
    )
)