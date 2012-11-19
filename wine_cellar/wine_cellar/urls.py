from django.conf.urls import patterns, include, url
import os
# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'wine_cellar.views.home', name='home'),
    url(r'^api/', include('wine_cellar.wines.urls')),
    url(r'^wines/', include('wine_cellar.wines.urls')),
    url(r'^$', 'wine_cellar.wines.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^pics/(.*)$',     'django.views.static.serve', {'document_root': os.path.join(settings.ROOT_PATH, "wines/media/img")}),
                            )
