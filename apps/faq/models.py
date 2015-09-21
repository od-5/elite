# coding=utf-8
from django.db import models
from pytils.translit import slugify
from core.models import Common

__author__ = 'alexy'


class FAQ(Common):
    class Meta:
        verbose_name = u'Вопрос и ответ'
        verbose_name_plural = u'Вопросы и ответы'
        app_label = 'faq'

    def __unicode__(self):
        return self.question[:100]

    def save(self):
        self.slug = slugify(self.question[:30])
        super(FAQ, self).save()

    def get_absolute_url(self):
        return u"/faq/%s" % self.slug

    question = models.TextField(verbose_name=u'Вопрос')
    answer = models.TextField(verbose_name=u'Ответ')
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)
