# coding=utf-8
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from django.conf import settings

__author__ = 'alexy'


class Slider(models.Model):
    image = models.ImageField(upload_to='slider', verbose_name=u'Слайд')
    image_resize = ImageSpecField(
        [SmartResize(*settings.SLIDER_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )

    def __unicode__(self):
        return u'Изображение #%s' % self.id

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image_resize.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True

    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'
        app_label = 'slider'