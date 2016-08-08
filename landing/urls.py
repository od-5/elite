# coding=utf-8
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.contrib import admin
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView, ListView, DetailView
from apps.article.models import Article
from apps.faq.models import FAQ

urlpatterns = patterns(
    '',
    url(r'^$', 'core.views.index', name='home'),
    url(r'^article/$', ListView.as_view(model=Article), name='article-list'),
    url(r'^article/(?P<slug>[\w-]+)$', DetailView.as_view(model=Article), name='article-detail'),
    url(r'^faq/$', ListView.as_view(model=FAQ), name='faq-list'),
    url(r'^faq/(?P<slug>[\w-]+)$', DetailView.as_view(model=FAQ), name='faq-detail'),
    url(r'^ticket/$', 'core.ajax.ticket_form', name='ticket'),
    url(r'^address/(?P<pk>\d+)/$', 'apps.address.ajax.address_item_list', name='address'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^data-import/', 'core.data_import.address_list_import', name='data-import'),
    url(r'^city/', include('apps.city.urls', namespace='city'),),
)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += staticfiles_urlpatterns()
