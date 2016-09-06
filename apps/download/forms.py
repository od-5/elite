from django.forms import ModelForm
from .models import MailTicket

__author__ = 'alexy'


class MailTicketTicketForm(ModelForm):
    class Meta:
        model = MailTicket
        fields = ('email',)
