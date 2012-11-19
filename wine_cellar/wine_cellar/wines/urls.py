from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = patterns('wine_cellar.wines.views',
                       url(r'^$', 'wine_list'),
                       )

urlpatterns = format_suffix_patterns( urlpatterns )