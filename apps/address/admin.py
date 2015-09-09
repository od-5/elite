from django.contrib import admin
from .models import Address, AddressItem

__author__ = 'alexy'


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'pic', )


class AddressItemAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pic')

admin.site.register(Address, AddressAdmin)
admin.site.register(AddressItem, AddressItemAdmin)
