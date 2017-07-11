# coding: utf-8
from annoying.decorators import ajax_request
from django.conf import settings
from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from apps.franchise.models import FranchiseSetup
from core.models import Setup
from .forms import MailTicketTicketForm


__author__ = 'alexy'


@ajax_request
@csrf_exempt
def bp_download(request):
    if request.method == 'POST':
        if request.POST.get('email'):
            form = MailTicketTicketForm(data=request.POST)
            if form.is_valid():
                form.save()
                # print 'valid'
                message = u'email: %s, телефон: %s' % (form.cleaned_data.get('email'), form.cleaned_data.get('phone'))
                try:
                    email = FranchiseSetup.objects.first().email
                except:
                    email = 'noreply@example.com'
                # print settings.EMAIL_HOST_USER
                email = 'od-5@yandex.ru'
                send_mail(
                    u'elitkadom.ru - оставлен email',
                    message,
                    settings.EMAIL_HOST_USER,
                    [email, ]
                )
                file = FranchiseSetup.objects.first().bp.url
                if not file:
                    file = u'/static/art-lift.pdf'
                return {
                    'success': True,
                    'file': file
                }
    else:
        return {
            'error': True
        }
