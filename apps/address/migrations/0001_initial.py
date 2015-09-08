# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20150908_1349'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=255, verbose_name='\u0410\u0434\u0440\u0435\u0441')),
                ('image', models.ImageField(upload_to=b'address', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('area', models.ForeignKey(verbose_name='\u0410\u0434\u0440\u0435\u0441', to='core.Area')),
            ],
            options={
                'verbose_name': '\u0410\u0434\u0440\u0435\u0441',
                'verbose_name_plural': '\u0410\u0434\u0440\u0435\u0441\u0430',
            },
            bases=(models.Model,),
        ),
    ]
