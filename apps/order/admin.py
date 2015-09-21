from django.contrib import admin
from .models import Order

__author__ = 'alexy'


class OrderAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'pic')

admin.site.register(Order, OrderAdmin)
