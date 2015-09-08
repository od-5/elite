# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Sale',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='commission',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='email',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='price',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='sale',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='sale_comment',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='sale_status',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_comment',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='ticket_status',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='total_price',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='travel_end',
        ),
        migrations.RemoveField(
            model_name='ticket',
            name='travel_start',
        ),
        migrations.AddField(
            model_name='ticket',
            name='phone',
            field=models.CharField(default='', max_length=256, verbose_name='\u0422\u0435\u043b\u0435\u0444\u043e\u043d'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438', blank=True, choices=[(0, '\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435'), (1, '\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430'), (2, '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e'), (3, '\u041e\u0442\u043c\u0435\u043d\u0430')]),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='ticket',
            name='comment',
            field=models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True),
        ),
    ]
