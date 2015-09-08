from django.contrib import admin
from .models import Address

__author__ = 'alexy'


class AddressAdmin(admin.ModelAdmin):
    list_display = ('address', 'area', 'pic', )


admin.site.register(Address, AddressAdmin)
