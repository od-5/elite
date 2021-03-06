from django.forms import ModelForm, HiddenInput
from core.models import Ticket

__author__ = 'alexy'


class MainTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone', 'email', 'comment')

    def __init__(self, *args, **kwargs):
        super(MainTicketForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True


class CityTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('name', 'phone', 'email', 'comment', 'city')
        widgets = {
            'city': HiddenInput(),
        }

    def __init__(self, *args, **kwargs):
        super(CityTicketForm, self).__init__(*args, **kwargs)
        self.fields['email'].required = True
