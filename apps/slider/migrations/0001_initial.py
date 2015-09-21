# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('image', models.ImageField(upload_to=b'slider', verbose_name='\u0421\u043b\u0430\u0439\u0434')),
                ('avatar_thumbnail', imagekit.models.fields.ProcessedImageField(upload_to=b'avatars')),
            ],
            options={
                'verbose_name': '\u0421\u043b\u0430\u0439\u0434',
                'verbose_name_plural': '\u0421\u043b\u0430\u0439\u0434\u044b',
            },
            bases=(models.Model,),
        ),
    ]
