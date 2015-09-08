# coding=utf-8
from django.db import models
from core.models import Area

__author__ = 'alexy'


class Address(models.Model):
    address = models.CharField(max_length=255, verbose_name=u'Адрес')
    area = models.ForeignKey(to=Area, verbose_name=u'Адрес')
    image = models.ImageField(upload_to='address', verbose_name=u'Изображение')

    def __unicode__(self):
        return self.address

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True

    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'
        app_label = 'address'
