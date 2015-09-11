# coding=utf-8
from django.db import models
from core.models import Area
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from django.conf import settings


__author__ = 'alexy'


class Address(models.Model):
    class Meta:
        verbose_name = u'Адрес'
        verbose_name_plural = u'Адреса'
        app_label = 'address'

    address = models.CharField(max_length=255, verbose_name=u'Адрес')
    image = models.ImageField(upload_to='address', verbose_name=u'Изображение')
    image_resize = ImageSpecField(
        [SmartResize(*settings.ADDRESS_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    def __unicode__(self):
        return self.address

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True




class AddressItem(models.Model):
    class Meta:
        verbose_name = u'Реклама'
        verbose_name_plural = u'Реклама'
        app_label = 'address'

    address = models.ForeignKey(to=Address, verbose_name=u'Адрес')
    image = models.ImageField(upload_to='addressitem', verbose_name=u'Изображение')
    image_resize = ImageSpecField(
        [SmartResize(*settings.ADDRESS_ITEM_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    def __unicode__(self):
        return self.address.address

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True
