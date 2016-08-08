# coding=utf-8
from django.conf.urls import patterns, url
from apps.city.ajax import get_city_list

__author__ = 'alexy'

urlpatterns = patterns(
    '',
    url(r'^get_city_list/$', get_city_list, name='get_city_list'),
    # url(r'^import/$', import_view, name='import'),

    url(r'^(?P<slug>[\w-]+)/$', 'core.views.index', name='view'),
)
