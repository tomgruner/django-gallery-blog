from django.conf.urls.defaults import patterns,  url

from . import views

 
urlpatterns = patterns('',
     url(r'^$', views.list_view),
     url(r'^tag/(?P<tag_slug>[-\w]+)$', views.list_view),
     url(r'^(?P<slug>[-\w]+)$', views.single_entry),
)