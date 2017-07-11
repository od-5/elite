from django.contrib import admin
from .models import MailTicket

__author__ = 'alexy'


class MailTicketAdmin(admin.ModelAdmin):
    list_display = ('email', 'phone', 'created', )
    date_hierarchy = 'created'


admin.site.register(MailTicket, MailTicketAdmin)
