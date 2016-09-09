# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin
from django import forms
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import Block1, Block2, Client, Block3, Block4, Block5, Block6

__author__ = 'alexy'


class Block1Admin(SortableModelAdmin):
    list_display = ('text',)
    sortable = 'order'


class Block2Admin(SortableModelAdmin):
    list_display = ('stand', 'price')
    sortable = 'order'


class ClientAdmin(SortableModelAdmin):
    list_display = ('__unicode__',)
    sortable = 'order'


class Block3Admin(SortableModelAdmin):
    list_display = ('text',)
    sortable = 'order'


class Block4Admin(SortableModelAdmin):
    list_display = ('text',)
    sortable = 'order'


class Block5Admin(SortableModelAdmin):
    list_display = ('text', 'price')
    sortable = 'order'


class Block6Admin(SortableModelAdmin):
    list_display = ('text',)
    sortable = 'order'


admin.site.register(Block1, Block1Admin)
admin.site.register(Block2, Block2Admin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Block3, Block3Admin)
admin.site.register(Block4, Block4Admin)
admin.site.register(Block5, Block5Admin)
admin.site.register(Block6, Block6Admin)
