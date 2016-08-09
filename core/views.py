from django.shortcuts import render
from apps.address.models import Address
from apps.city.models import City
from apps.order.models import Order
from apps.review.models import FileReview, TextReview
from apps.slider.models import Slider
from apps.advantages.models import Advantage
from apps.video.models import Video
from core.forms import MainTicketForm, CityTicketForm

__author__ = 'alexey'


def index(request, slug=None):
    # slider = Slider.objects.all()
    if slug:
        current_city = City.objects.get(slug=slug)
    else:
        current_city = None
    if current_city:
        request.session['current_city'] = current_city.id
        address = Address.objects.filter(city=current_city)
        filrereview_qs = FileReview.objects.filter(city=current_city)
        textreview_qs = TextReview.objects.filter(city=current_city)
    else:
        request.session['current_city'] = False
        address = Address.objects.filter(city__isnull=True)
        filrereview_qs = FileReview.objects.filter(city__isnull=True)
        textreview_qs = TextReview.objects.filter(city__isnull=True)
    video_qs = Video.objects.all()
    advantage_list = Advantage.objects.all()
    order_qs = Order.objects.all()
    if current_city:
        form = CityTicketForm(initial={'city': current_city.id})
    else:
        form = MainTicketForm()
    return render(request, 'index.html', {
        'form': form,
        'video_list': video_qs,
        'address_list': address,
        'advantage_list': advantage_list,
        'order_list': order_qs,
        'current_city': current_city,
        'filereview_list': filrereview_qs,
        'textreview_list': textreview_qs
    })
