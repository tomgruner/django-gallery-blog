from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mirto.views.home', name='home'),
    # url(r'^mirto/', include('mirto.foo.urls')),

     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
     url(r'^admin/', include(admin.site.urls)),
     url(r'^grappelli/', include('grappelli.urls')),
     url(r'', include('apps.content.urls')),
)


#THIS IS FOR DEVELOPMENT STATIC MEDIA
# -----------------------------------
if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^media/(?P<path>.*)$',
            'django.views.static.serve',
            {
                'document_root': settings.MEDIA_ROOT,
                'show_indexes': True
            }
        ),
    )
# -----------------------------------
