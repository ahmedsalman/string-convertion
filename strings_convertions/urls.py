from django.conf.urls import patterns, include, url

from rest_framework import routers

from strings_convertions.views import home, MyRESTView


urlpatterns = patterns(
    '',
    url(r'^$', home, name='home'),
    url(r'^restfull-api/$', MyRESTView.as_view(), name='restfull_api'),
)
