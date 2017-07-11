# coding=utf-8
from django.db import models
from django.conf import settings
from core.models import Common

__author__ = 'alexy'


class MailTicket(Common):
    class Meta:
        verbose_name = u'Оставленный e-mail'
        verbose_name_plural = u'Оставленные e-mail'
        app_label = 'download'

    phone = models.CharField(verbose_name=u'Телефон', max_length=100)
    email = models.EmailField(verbose_name=u'E-mail', max_length=100)

    def __unicode__(self):
        return self.email
