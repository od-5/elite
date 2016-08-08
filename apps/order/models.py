# coding=utf-8
from PIL import Image
from django.db import models
from imagekit.models import ImageSpecField
from pilkit.processors import SmartResize
from django.conf import settings

__author__ = 'alexy'


class Order(models.Model):
    class Meta:
        verbose_name = u'Пункт заказа'
        verbose_name_plural = u'Пункты заказа'
        app_label = 'order'

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Order, self).save()
        if self.image:
            image = Image.open(self.image)
            (width, height) = image.size
            size = (320, 320)
            "Max width and height 200"
            if width > 320:
                image.thumbnail(size, Image.ANTIALIAS)
                image.save(self.image.path, "PNG")

    def pic(self):
        return '<img src="%s" width="170"/>' % self.image.url
    pic.short_description = u"Иконка"
    pic.allow_tags = True

    title = models.CharField(verbose_name=u'Заголовок', max_length=256)
    link = models.CharField(verbose_name=u'Ссылка', max_length=256, blank=True, null=True)
    image = models.ImageField(upload_to='order', verbose_name=u'Картинка')
    image_resize = ImageSpecField(
        [SmartResize(*settings.ORDER_ITEM_SIZE)], source='image', format='JPEG', options={'quality': 94}
    )
