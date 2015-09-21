# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='slider',
            name='avatar_thumbnail',
        ),
    ]
