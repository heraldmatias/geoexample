# -*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, include, url
from django.contrib.gis import admin
from django.conf import settings
admin.autodiscover()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),    
    (r'^grappelli/', include('grappelli.urls')),    
)

from django.views.static import serve
urlpatterns += patterns('',
    url(r'^media/(?P<path>.*)$',
        serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'^static/(?P<path>.*)$',
        serve, {'document_root': settings.STATIC_ROOT}),
    url(r'^favicon\.ico$', 
        'django.views.generic.simple.redirect_to', 
        {'url': '/static/images/favicon.ico'}),
)