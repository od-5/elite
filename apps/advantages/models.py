# coding=utf-8
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from django.conf import settings

__author__ = 'alexy'


class Advantage(models.Model):
    class Meta:
        verbose_name = u'Преимущество'
        verbose_name_plural = u'Преимущества'
        app_label = 'advantages'

    def __unicode__(self):
        return self.title

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url
    pic.short_description = u"Иконка"
    pic.allow_tags = True

    title = models.CharField(verbose_name=u'Заголовок', max_length=256)
    link = models.CharField(verbose_name=u'Ссылка', max_length=256, blank=True, null=True)
    text = models.TextField(verbose_name=u'Текст', blank=True, null=True)
    image = models.ImageField(upload_to='slider', verbose_name=u'Слайд')
    image_resize = ImageSpecField(
        [SmartResize(*settings.SLIDER_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )
