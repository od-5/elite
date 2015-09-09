# coding=utf-8
from django.db import models

__author__ = 'alexey'


class Common(models.Model):
    created = models.DateField(verbose_name=u'Дата создания', auto_now=True)


class Area(models.Model):
    class Meta:
        verbose_name = u'Район'
        verbose_name_plural = u'Район'
        app_label = 'core'

    def __unicode__(self):
        return self.title

    title = models.CharField(max_length=255, verbose_name=u'Название')


class Ticket(Common):
    class Meta:
        verbose_name = u'Заявка'
        verbose_name_plural = u'Заявки'
        app_label = 'core'

    def __unicode__(self):
        return self.name

    TICKET_STATUS_CHOICE = (
        (0, u'В обработке'),
        (1, u'Новая заявка'),
        (2, u'Выполнено'),
        (3, u'Отмена'),
    )

    name = models.CharField(verbose_name=u'Имя', max_length=256)
    phone = models.CharField(verbose_name=u'Телефон', max_length=256)
    area = models.ForeignKey(to=Area, verbose_name=u'Район', blank=True, null=True)
    status = models.PositiveSmallIntegerField(verbose_name=u'Статус заявки',  choices=TICKET_STATUS_CHOICE, default=0, blank=True, null=True)
    comment = models.TextField(verbose_name=u'Комментарий', blank=True, null=True)


class Contacts(models.Model):
    class Meta:
        verbose_name = u'Контакты'
        verbose_name_plural = u'Контакты'
        app_label = 'core'

    def __unicode__(self):
        if self.phone:
            return self.phone
        elif self.email:
            return self.email
        elif self.address:
            return self.address
        else:
            return u'Контакты'

    phone = models.CharField(max_length=30, verbose_name=u'Телефон', blank=True, null=True)
    email = models.EmailField(max_length=50, verbose_name=u'e-mail', blank=True, null=True)
    address = models.TextField(verbose_name=u'Адрес', blank=True, null=True)


class Setup(models.Model):
    class Meta:
        verbose_name = u'Настройки сайта'
        verbose_name_plural = u'Настройки сайта'
        app_label = 'core'

    def __unicode__(self):
        if self.title:
            return self.title
        else:
            return u'Настройки'

    title = models.CharField(verbose_name=u'Заголовок <TITLE>...</TITLE>', max_length=256, blank=True)
    email = models.EmailField(verbose_name=u'e-mail для приёма заявок', blank=True)
    video = models.TextField(verbose_name=u'HTML-код видео', blank=True, null=True)
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    top_js = models.TextField(verbose_name=u'Скрипты в <HEAD>..</HEAD>', blank=True)
    bottom_js = models.TextField(verbose_name=u'Скрипты перед закрывающим </BODY>', blank=True)
