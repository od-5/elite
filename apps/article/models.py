# coding=utf-8
from ckeditor.fields import RichTextField
from django.db import models
from pytils.translit import slugify
from core.models import Common

__author__ = 'alexy'


class Article(Common):
    class Meta:
        verbose_name = u'Статья'
        verbose_name_plural = u'Статьи'
        app_label = 'article'

    def __unicode__(self):
        return self.title

    def save(self):
        self.slug = slugify(self.title)
        super(Article, self).save()

    def get_absolute_url(self):
        return u"/article/%s" % self.slug

    title = models.CharField(verbose_name=u'Заголовок', max_length=256)
    text = RichTextField(verbose_name=u'Текст')
    meta_key = models.TextField(verbose_name=u'Ключевые слова META_KEYWORDS', blank=True)
    meta_desc = models.TextField(verbose_name=u'Описание META_DESCRIPTION', blank=True)
    slug = models.SlugField(max_length=100, verbose_name=u'url', blank=True)
