# coding: utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from core.models import Setup
from .forms import MailTicketTicketForm


__author__ = 'alexy'


@ajax_request
@csrf_exempt
def bp_download(request):
    if request.method == 'POST':
        r_email = request.POST.get('email')
        # print r_email
        if request.POST.get('email'):
            form = MailTicketTicketForm(data=request.POST)
            if form.is_valid():
                form.save()
                # print 'valid'
                message = u'email: %s' % r_email
                try:
                    email = Setup.objects.all()[0].email
                except:
                    email = 'noreply@example.com'
                # print settings.EMAIL_HOST_USER
                # email = 'od-5@yandex.ru'
                send_mail(
                    u'elitkadom.ru - оставлен email',
                    message,
                    settings.EMAIL_HOST_USER,
                    [email, ]
                )
        return {
            'success': True
        }
    else:
        return {
            'error': True
        }