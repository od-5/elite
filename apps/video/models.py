# coding=utf-8
from django.db import models
from apps.city.models import City

__author__ = 'alexy'


class Video(models.Model):
    class Meta:
        verbose_name = u'Видео'
        verbose_name_plural = u'Видео'
        app_label = 'video'

    def __unicode__(self):
        return self.name

    city = models.ForeignKey(to=City, verbose_name=u'Город', blank=True, null=True)
    name = models.CharField(max_length=256, verbose_name=u'Название')
    code = models.TextField(verbose_name=u'Код видео')
    order = models.PositiveIntegerField(default=1, verbose_name=u'Сортировка')
