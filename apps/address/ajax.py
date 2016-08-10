from annoying.decorators import ajax_request
from django.views.decorators.csrf import csrf_exempt
from .models import AddressItem

__author__ = 'alexy'


@ajax_request
@csrf_exempt
def address_item_list(request, pk):
    # if request.method == 'POST':
    #     address = request.POST.get('address')
    #     print address
    #     address_qs = AddressItem.objects.filter(address=int(address))
    #     address_list = []
    #     for i in address_qs:
    #         address_list.append(i.image_resize.url)
    #     return {
    #         'success': address_list
    #     }
    pk = int(pk)
    address_qs = AddressItem.objects.filter(address=int(pk))
    address_list = []
    for i in address_qs:
        address_list.append(str(i.image_resize.url))
    return address_list
