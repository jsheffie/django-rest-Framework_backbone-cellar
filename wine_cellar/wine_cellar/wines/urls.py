from django.conf.urls import patterns, url
from rest_framework.urlpatterns import format_suffix_patterns
from wine_cellar.wines import views

urlpatterns = patterns('',
                       url(r'^$', views.WineList.as_view()),
                       )

urlpatterns = format_suffix_patterns( urlpatterns )