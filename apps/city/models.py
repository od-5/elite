# coding=utf-8
import datetime
from django.conf import settings
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.urlresolvers import reverse
from django.db import models
from pytils.translit import slugify
import core.geotagging as api

__author__ = 'alexy'

api_key = settings.YANDEX_MAPS_API_KEY


class City(models.Model):
    class Meta:
        verbose_name = u'Город'
        verbose_name_plural = u'Города'
        app_label = 'city'

    def __unicode__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('city', args=(self.slug,))

    def save(self, *args, **kwargs):
        address = u'город %s' % self.name
        pos = api.geocode(api_key, address)
        self.coord_y = float(pos[0])
        self.coord_x = float(pos[1])
        super(City, self).save()

    name = models.CharField(max_length=100, verbose_name=u'Город')
    manager = models.ForeignKey(to=User, blank=True, null=True, verbose_name=u'Руководитель филиала')
    email = models.EmailField(max_length=100, blank=True, null=True, verbose_name=u'Email для приёма заявок')
    phone = models.CharField(max_length=20, blank=True, null=True, verbose_name=u'Контактный телефон')
    coord_x = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Широта')
    coord_y = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Долгота')
    slug = models.SlugField(verbose_name=u'url', blank=True, null=True, max_length=50)


class CityArea(models.Model):
    class Meta:
        verbose_name = u'Район'
        verbose_name_plural = u'Районы'
        app_label = 'city'

    def __unicode__(self):
        return self.name

    city = models.ForeignKey(to=City, verbose_name=u'Город')
    name = models.CharField(max_length=100, verbose_name=u'Название')


class CityStreet(models.Model):
    class Meta:
        verbose_name = u'Улица'
        verbose_name_plural = u'Улицы'
        app_label = 'city'

    def __unicode__(self):
        return self.name

    city = models.ForeignKey(to=City, verbose_name=u'Город')
    area = models.ForeignKey(to=CityArea, verbose_name=u'Район')
    name = models.CharField(max_length=100, verbose_name=u'Название')


class CityHouse(models.Model):
    class Meta:
        verbose_name = u'Дом'
        verbose_name_plural = u'Дома'
        app_label = 'city'

    def __unicode__(self):
        return self.number

    def full_address(self):
        address = u'город %s %s %s' % (self.city.name, self.street.name, self.number)
        return address

    def save(self, *args, **kwargs):
        address = u'город %s %s %s' % (self.city.name, self.street.name, self.number)
        pos = api.geocode(api_key, address)
        self.coord_y = float(pos[0])
        self.coord_x = float(pos[1])
        super(CityHouse, self).save()

    city = models.ForeignKey(to=City, verbose_name=u'Город')
    area = models.ForeignKey(to=CityArea, verbose_name=u'Район')
    street = models.ForeignKey(to=CityStreet, verbose_name=u'Улица')
    number = models.CharField(max_length=10, verbose_name=u'Номер дома')
    coord_x = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Широта')
    coord_y = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True, verbose_name=u'Долгота')