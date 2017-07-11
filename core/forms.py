from django.forms import ModelForm, HiddenInput
from core.models import Ticket

__author__ = 'alexy'


class MainTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone', 'email', 'comment')


class CityTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone', 'email', 'comment', 'city')
        widgets = {
            'city': HiddenInput(),
        }
