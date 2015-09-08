from django.contrib import admin
from .models import Slider

__author__ = 'alexy'


class SliderAdmin(admin.ModelAdmin):
    list_display = ('__unicode__', 'pic', )


admin.site.register(Slider, SliderAdmin)
