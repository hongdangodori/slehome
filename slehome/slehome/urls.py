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
    url(r'^sle/photo/', include('photo.urls'), name="photos"),
    url(r'^sle/', include('account.urls'), name="account"),
    url(r'^sle/infoboards/', include('infoboards.urls'), name="infoboards"),
    url(r'^sle/imagecrop/', include('imagecrop.urls'), name="imagecrop"),
)

urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
    	{'document_root': settings.MEDIA_ROOT}
    ),
)

# urlpatterns += patterns('',
# 	url(r'^[a-zA-Z1-9가-힣][a-zA-Z1-9/가-힣]*', 'exception.views.exception_page'),
# )