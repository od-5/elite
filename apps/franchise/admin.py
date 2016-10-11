# coding=utf-8
from django.contrib import admin
from suit.admin import SortableModelAdmin
from django import forms
from nested_inline.admin import NestedStackedInline, NestedModelAdmin, NestedTabularInline
from .models import Block1, Block2, Client, Block3, Block4, Block5, Block6, FranchiseSetup, Block41

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


class Block41Admin(SortableModelAdmin):
    list_display = ('name', 'cost')
    filter_horizontal = ['item',]
    sortable = 'order'


class Block5Admin(SortableModelAdmin):
    list_display = ('text', 'price')
    sortable = 'order'


class Block6Admin(SortableModelAdmin):
    list_display = ('text',)
    sortable = 'order'


class FranchiseSetupAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'title', 'email', 'phone')

    def has_add_permission(self, request):
        if FranchiseSetup.objects.count() >= 1:
            return False
        else:
            return True


admin.site.register(Block1, Block1Admin)
admin.site.register(Block2, Block2Admin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Block3, Block3Admin)
admin.site.register(Block4, Block4Admin)
admin.site.register(Block41, Block41Admin)
admin.site.register(Block5, Block5Admin)
admin.site.register(Block6, Block6Admin)
admin.site.register(FranchiseSetup, FranchiseSetupAdmin)
