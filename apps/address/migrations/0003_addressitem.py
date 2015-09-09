# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('address', '0002_remove_address_area'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddressItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'addressitem', verbose_name='\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435')),
                ('address', models.ForeignKey(verbose_name='\u0410\u0434\u0440\u0435\u0441', to='address.Address')),
            ],
            options={
                'verbose_name': '\u0420\u0435\u043a\u043b\u0430\u043c\u0430',
                'verbose_name_plural': '\u0420\u0435\u043a\u043b\u0430\u043c\u0430',
            },
            bases=(models.Model,),
        ),
    ]
