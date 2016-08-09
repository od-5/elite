# coding: utf-8
from apps.city.models import City
from .models import Setup, Contacts


__author__ = 'alexy'


def site_setup(request):
    try:
        request.session['current_city']
    except:
        request.session['current_city'] = False
    current_city = int(request.session['current_city'])
    print current_city
    setup = Setup.objects.first()
    if current_city == 0:
        contact = Contacts.objects.first()
        phone = contact.phone
        email = contact.email
        address = contact.address
    else:
        city = City.objects.get(pk=current_city)
        if city.phone:
            phone = city.phone
        else:
            phone = Contacts.objects.first().phone
        if city.email:
            email = city.email
        else:
            email = Contacts.objects.first().email
        if city.legal_address:
            address = city.legal_address
        else:
            address = Contacts.objects.first().address
    return {
        'SETUP': setup,
        'PHONE': phone,
        'EMAIL': email,
        'ADDRESS': address
    }
