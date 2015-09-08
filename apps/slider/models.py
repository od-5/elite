# coding=utf-8
from django.db import models

__author__ = 'alexy'


class Slider(models.Model):
    image = models.ImageField(upload_to='slider', verbose_name=u'Слайд')

    def __unicode__(self):
        return u'Изображение #%s' % self.id

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True

    class Meta:
        verbose_name = u'Слайд'
        verbose_name_plural = u'Слайды'
        app_label = 'slider'