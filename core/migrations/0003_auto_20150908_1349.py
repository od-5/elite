# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20150908_1340'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=255, verbose_name='\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435')),
            ],
            options={
                'verbose_name': '\u0420\u0430\u0439\u043e\u043d',
                'verbose_name_plural': '\u0420\u0430\u0439\u043e\u043d',
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='ticket',
            name='area',
            field=models.ForeignKey(verbose_name='\u0420\u0430\u0439\u043e\u043d', blank=True, to='core.Area', null=True),
            preserve_default=True,
        ),
    ]
