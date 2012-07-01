from django.conf.urls.defaults import patterns,  url

from . import views

urlpatterns = patterns('',
     url(r'^$', views.list_by_columns),
     url(r'^tag/(?P<tag_slug>[-\w]+)$', views.list_by_columns),
     url(r'^(?P<slug>[-\w]+)$', views.single_entry),
)