from django.contrib import admin
from .models import Advantage

__author__ = 'alexy'


class AdvantageAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'text', 'pic')

admin.site.register(Advantage, AdvantageAdmin)
