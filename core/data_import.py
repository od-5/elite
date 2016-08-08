# coding=utf-8
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import redirect
import pyexcel
from apps.city.models import City, CityArea, CityStreet, CityHouse
import pyexcel_xls
import pyexcel_xlsx
# import pyexcel_xls.xls
# import pyexcel_xlsx.xlsx
# from pyexcel.ext import xls

__author__ = 'alexy'


def address_list_import(request):
    if request.method == 'POST' and 'file' in request.FILES:
        filename = request.FILES['file'].name
        extension = filename.split(".")[1]
        sheet = pyexcel.load_from_memory(extension, request.FILES['file'].read())
        data = pyexcel.to_dict(sheet)
        for row in data:
            if row != 'Series_1':
                city = data[row][0]
                area = data[row][1]
                street = data[row][2]
                house_number = ''
                point_flag = False
                for i in unicode(data[row][3]):
                    if i == '.':
                        point_flag = True
                    if point_flag:
                        if i != '0' and i != '.':
                            house_number += i
                    else:
                        house_number += i
                print city
                print area
                print street
                print house_number

                try:
                    # пробуем получить город
                    city_instance = City.objects.get(name__iexact=city)
                    print 'has city_instance: %s' % city_instance
                    try:
                        # пробуем получить район
                        area_instance = CityArea.objects.get(city=city_instance, name__iexact=area)
                        print 'has area_instance: %s' % area_instance
                    except:
                        # создаём новый район
                        area_instance = CityArea(city=city_instance, name=area)
                        area_instance.save()
                        print 'create area_instance: %s' % area_instance
                    try:
                        # пробуем получить улицу
                        street_instance = CityStreet.objects.get(city=city_instance, area=area_instance, name__iexact=street)
                        print 'has street_instance: %s' % street_instance
                    except:
                        # создаём новую улицу
                        street_instance = CityStreet(city=city_instance, area=area_instance, name=street)
                        street_instance.save()
                        print 'create street_instance: %s' % street_instance
                    try:
                        # пробуем получить поверхность
                        house_instance = CityHouse.objects.get(city=city_instance, area=area_instance, street=street_instance,
                                                               number=house_number)
                        print 'has house_instance: %s' % house_instance
                    except:
                        # создаём поверхность
                        house_instance = CityHouse(city=city_instance, area=area_instance, street=street_instance, number=house_number)
                        house_instance.save()
                        print 'create house_instance: %s' % house_instance
                except:
                    pass
                    print u'Город не найден'
                    return HttpResponseRedirect(reverse('admin-index'))
        return HttpResponseRedirect('/admin/city/cityhouse/')
