# coding=utf-8
from annoying.decorators import ajax_request
from apps.city.models import City
__author__ = 'alexy'


# def import_view(request):
#     return render('')


@ajax_request
def get_city_list(request):
    """
    Функция получения информации для карты главной страницы сайта
    Получение полного списка городов с координатами.
    """
    qs = City.objects.all()
    city_list = []
    for city in qs:
        city_list.append({
            'name': city.name,
            'coord_x': float(city.coord_x),
            'coord_y': float(city.coord_y),
            'house_count': city.cityhouse_set.count()
        })
    return {
        'city_list': city_list
    }
