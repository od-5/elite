# coding=utf-8
from PIL import Image
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from django.conf import settings
from apps.city.models import City

__author__ = 'alexy'


class FileReview(models.Model):
    class Meta:
        verbose_name = u'Скан'
        verbose_name_plural = u'Сканы'
        app_label = 'review'

    def __unicode__(self):
        return u'Изображение #%s' % self.id

    def save(self, *args, **kwargs):
        super(FileReview, self).save()
        if self.image:
            image = Image.open(self.image)
            (width, height) = image.size
            size = (800, 800)
            "Max width and height 200"
            if width > 800:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.image.path, "PNG")

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image_resize.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True

    city = models.ForeignKey(to=City, verbose_name=u'Город', blank=True, null=True)
    name = models.CharField(max_length=256, verbose_name=u'Название')
    image = models.ImageField(upload_to='review', verbose_name=u'Скан отзыва')
    image_resize = ImageSpecField(
        [SmartResize(*settings.REVIEW_ITEM_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )


class TextReview(models.Model):
    class Meta:
        verbose_name = u'Текстовый отзыв'
        verbose_name_plural = u'Текстовые отзывы'
        app_label = 'review'

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        super(TextReview, self).save()
        if self.image:
            image = Image.open(self.image)
            (width, height) = image.size
            size = (100, 100)
            "Max width and height 200"
            if width > 100:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.image.path, "PNG")

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image_resize.url
    pic.short_description = u"Миниатюра"
    pic.allow_tags = True

    city = models.ForeignKey(to=City, verbose_name=u'Город', blank=True, null=True)
    name = models.CharField(max_length=256, verbose_name=u'ФИО')
    company = models.CharField(max_length=256, verbose_name=u'Организация')
    text = models.TextField(verbose_name=u'Текст')
    image = models.ImageField(upload_to='review', verbose_name=u'Фотография')
    image_resize = ImageSpecField(
        [SmartResize(*settings.REVIEW_AVATAR_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )
