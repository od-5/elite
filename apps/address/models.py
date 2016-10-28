# coding=utf-8
from PIL import Image
from django.db import models
from apps.city.models import City
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

    city = models.ForeignKey(to=City, verbose_name=u'Город', blank=True, null=True)
    address = models.CharField(max_length=255, verbose_name=u'Адрес')
    image = models.ImageField(upload_to='address', verbose_name=u'Изображение')
    image_resize = ImageSpecField(
        [SmartResize(*settings.ADDRESS_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    def __unicode__(self):
        return self.address

    def save(self, *args, **kwargs):
        super(Address, self).save()
        if self.image:
            image = Image.open(self.image)
            (width, height) = image.size
            size = (800, 800)
            "Max width and height 200"
            if width > 800:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.image.path, "PNG")

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url

    def lift_count(self):
        return self.addressitem_set.count()

    pic.short_description = u"Миниатюра"
    pic.allow_tags = True
    lift_count.short_description = u"Количество фотографий"


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

    def save(self, *args, **kwargs):
        super(AddressItem, self).save()
        if self.image:
            image = Image.open(self.image)
            (width, height) = image.size
            size = (800, 800)
            "Max width and height 200"
            if width > 800:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.image.path, "PNG")

    def pic(self):
        return '<img src="%s" width="150"/>' % self.image.url

    def address_pic(self):
        return '<img src="%s" width="170"/>' % self.address.image.url

    pic.short_description = u"Миниатюра"
    pic.allow_tags = True
    address_pic.short_description = u"Адрес"
    address_pic.allow_tags = True