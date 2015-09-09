from django.shortcuts import render
from apps.address.models import Address
from apps.slider.models import Slider
from core.forms import TicketForm

__author__ = 'alexey'


def index(request):
    slider = Slider.objects.all()
    address = Address.objects.all()
    form = TicketForm()
    return render(request, 'index.html', {
        'form': form,
        'slider': slider,
        'address_list': address,
    })