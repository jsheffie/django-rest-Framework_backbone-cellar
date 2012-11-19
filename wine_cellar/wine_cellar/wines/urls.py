from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from wine_cellar.wines import views
import os
urlpatterns = patterns('',
                       url(r'^wines/', views.WineList.as_view()),
                       )

urlpatterns = format_suffix_patterns( urlpatterns )

from django.conf import settings
if settings.DEBUG:
    urlpatterns += patterns('',
                            (r'^css/(.*)$',     'django.views.static.serve', {'document_root': os.path.join(settings.ROOT_PATH, "wines/media/css")}),
                            (r'^js/(.*)$',      'django.views.static.serve', {'document_root': os.path.join(settings.ROOT_PATH, "wines/media/js")}),
                            (r'^lib/(.*)$',      'django.views.static.serve', {'document_root': os.path.join(settings.ROOT_PATH, "wines/media/lib")}),
                            (r'^img/(.*)$',     'django.views.static.serve', {'document_root': os.path.join(settings.ROOT_PATH, "wines/media/img")}),
                            )
