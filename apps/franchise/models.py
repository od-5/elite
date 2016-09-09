# coding=utf-8
# import datetime
# from PIL import Image
# from django.conf import settings
# from django.dispatch import receiver
# from django.core.urlresolvers import reverse
from django.db import models

__author__ = 'alexy'


class Block1(models.Model):
    class Meta:
        verbose_name = u'Новая модель размещения рекламы в лифте'
        verbose_name_plural = u'Новая модель размещения рекламы в лифте'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')


class Block2(models.Model):
    class Meta:
        verbose_name = u'Доходность третьего этапа'
        verbose_name_plural = u'Доходность третьего этапа'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return str(self.stand)

    stand = models.IntegerField(verbose_name=u'Количество стендов')
    price = models.IntegerField(verbose_name=u'Цена')
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')


class Client(models.Model):
    class Meta:
        verbose_name = u'Наши клиенты'
        verbose_name_plural = u'Наши клиенты'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return self.img.url

    img = models.ImageField(upload_to='franchise', verbose_name=u'Изображение')
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')


class Block3(models.Model):
    class Meta:
        verbose_name = u'Купив нашу франшизу вы получите'
        verbose_name_plural = u'Купив нашу франшизу вы получите'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    icon = models.ImageField(upload_to='franchise', verbose_name=u'Иконка')
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')


class Block4(models.Model):
    class Meta:
        verbose_name = u'Комплектация франшизы'
        verbose_name_plural = u'Комплектация франшизы'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')


class Block5(models.Model):
    class Meta:
        verbose_name = u'Дополнительные услуги'
        verbose_name_plural = u'Дополнительные услуги'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    price = models.CharField(verbose_name=u'Стоимость', max_length=100)
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')


class Block6(models.Model):
    class Meta:
        verbose_name = u'Преимущества'
        verbose_name_plural = u'Преимущества'
        app_label = 'franchise'
        ordering = ['order', ]

    def __unicode__(self):
        return self.text

    text = models.TextField(verbose_name=u'Текст')
    order = models.PositiveIntegerField(verbose_name=u'Сортировка')