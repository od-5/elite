# coding=utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from core.forms import TicketForm
from .models import Ticket, Setup

__author__ = 'alexy'


@ajax_request
def ticket_form(request):
    try:
        email = Setup.objects.all()[0].email
    except:
        email = 'od-5@yandex.ru'
    print email
    if request.method == "POST":
        form = TicketForm(data=request.POST)
        if form.is_valid():
            ticket = form.save(commit=False)
            ticket.status = 1
            ticket.save()
            message = u'Имя: %s\nТелефон: %s\n' % (ticket.name, ticket.phone)
            print settings.EMAIL_HOST_USER
            send_mail(
                u'Реклама в лифтах - Заявка с сайта',
                message,
                settings.EMAIL_HOST_USER,
                [email, ]
            )
            return {
                'success': True
            }
        else:
            return {
                'success': False
            }
    return {
        'success': False
    }
