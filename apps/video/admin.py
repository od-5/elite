# coding=utf-8
from django.contrib import admin
from .models import Video
from django.forms import ModelForm, Textarea
from suit.admin import SortableModelAdmin

__author__ = 'alexy'


class VideForm(ModelForm):
    class Meta:
        widgets = {
            'code': Textarea(attrs={'style': 'width:98%'}),
        }


class VideoAdmin(SortableModelAdmin):
    list_display = ('city', 'name', 'code',)
    list_filter = ('city',)
    form = VideForm
    sortable = 'order'


admin.site.register(Video, VideoAdmin)
