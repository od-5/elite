# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a')),
                ('link', models.CharField(max_length=256, null=True, verbose_name='\u0421\u0441\u044b\u043b\u043a\u0430', blank=True)),
                ('image', models.ImageField(upload_to=b'order', verbose_name='\u041a\u0430\u0440\u0442\u0438\u043d\u043a\u0430')),
            ],
            options={
                'verbose_name': '\u041f\u0443\u043d\u043a\u0442 \u0437\u0430\u043a\u0430\u0437\u0430',
                'verbose_name_plural': '\u041f\u0443\u043d\u043a\u0442\u044b \u0437\u0430\u043a\u0430\u0437\u0430',
            },
            bases=(models.Model,),
        ),
    ]
