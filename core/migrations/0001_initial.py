# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Common',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created', models.DateField(auto_now=True, verbose_name='\u0414\u0430\u0442\u0430 \u0441\u043e\u0437\u0434\u0430\u043d\u0438\u044f')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Setup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='\u0417\u0430\u0433\u043e\u043b\u043e\u0432\u043e\u043a <TITLE>...</TITLE>', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='e-mail \u0434\u043b\u044f \u043f\u0440\u0438\u0451\u043c\u0430 \u0437\u0430\u044f\u0432\u043e\u043a', blank=True)),
                ('video', models.TextField(null=True, verbose_name='HTML-\u043a\u043e\u0434 \u0432\u0438\u0434\u0435\u043e', blank=True)),
                ('meta_key', models.TextField(verbose_name='\u041a\u043b\u044e\u0447\u0435\u0432\u044b\u0435 \u0441\u043b\u043e\u0432\u0430 META_KEYWORDS', blank=True)),
                ('meta_desc', models.TextField(verbose_name='\u041e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 META_DESCRIPTION', blank=True)),
                ('top_js', models.TextField(verbose_name='\u0421\u043a\u0440\u0438\u043f\u0442\u044b \u0432 <HEAD>..</HEAD>', blank=True)),
                ('bottom_js', models.TextField(verbose_name='\u0421\u043a\u0440\u0438\u043f\u0442\u044b \u043f\u0435\u0440\u0435\u0434 \u0437\u0430\u043a\u0440\u044b\u0432\u0430\u044e\u0449\u0438\u043c </BODY>', blank=True)),
            ],
            options={
                'verbose_name': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
                'verbose_name_plural': '\u041d\u0430\u0441\u0442\u0440\u043e\u0439\u043a\u0438 \u0441\u0430\u0439\u0442\u0430',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('common_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='core.Common')),
                ('name', models.CharField(max_length=256, verbose_name='\u0418\u043c\u044f')),
                ('email', models.EmailField(max_length=256, verbose_name='e-mail')),
                ('comment', models.TextField(null=True, verbose_name='\u0421\u043e\u043e\u0431\u0449\u0435\u043d\u0438\u0435 \u043a\u043b\u0438\u0435\u043d\u0442\u0430', blank=True)),
                ('sale', models.BooleanField(default=False, verbose_name='\u041f\u0440\u043e\u0434\u0430\u0436\u0430')),
                ('ticket_status', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u0437\u0430\u044f\u0432\u043a\u0438', blank=True, choices=[(0, '\u0412 \u043e\u0431\u0440\u0430\u0431\u043e\u0442\u043a\u0435'), (1, '\u041d\u043e\u0432\u0430\u044f \u0437\u0430\u044f\u0432\u043a\u0430'), (2, '\u041e\u0442\u043a\u043b\u043e\u043d\u0435\u043d\u0430'), (3, '\u041d\u0435\u0442 \u043e\u0442\u0432\u0435\u0442\u0430')])),
                ('ticket_comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('travel_start', models.DateField(null=True, verbose_name='\u041d\u0430\u0447\u0430\u043b\u043e \u0442\u0443\u0440\u0430', blank=True)),
                ('travel_end', models.DateField(null=True, verbose_name='\u041a\u043e\u043d\u0435\u0446 \u0442\u0443\u0440\u0430', blank=True)),
                ('sale_status', models.PositiveSmallIntegerField(default=0, null=True, verbose_name='\u0421\u0442\u0430\u0442\u0443\u0441 \u043f\u0440\u043e\u0434\u0430\u0436\u0438', blank=True, choices=[(0, '\u041e\u0436\u0438\u0434\u0430\u043d\u0438\u0435 \u043e\u043f\u043b\u0430\u0442\u044b'), (1, '\u0423\u0442\u043e\u0447\u043d\u0435\u043d\u0438\u0435 \u0434\u0435\u0442\u0430\u043b\u0435\u0439'), (2, '\u041e\u043f\u043b\u0430\u0447\u0435\u043d\u043e')])),
                ('sale_comment', models.TextField(null=True, verbose_name='\u041a\u043e\u043c\u043c\u0435\u043d\u0442\u0430\u0440\u0438\u0439', blank=True)),
                ('price', models.PositiveIntegerField(default=0, null=True, verbose_name='\u0421\u0443\u043c\u043c\u0430', blank=True)),
                ('commission', models.PositiveIntegerField(default=0, null=True, verbose_name='\u041a\u043e\u043c\u043c\u0438\u0441\u0438\u044f', blank=True)),
                ('total_price', models.PositiveIntegerField(default=0, null=True, verbose_name='\u0418\u0442\u043e\u0433\u043e', blank=True)),
            ],
            options={
                'verbose_name': '\u0417\u0430\u044f\u0432\u043a\u0430',
                'verbose_name_plural': '\u0417\u0430\u044f\u0432\u043a\u0438',
            },
            bases=('core.common',),
        ),
        migrations.CreateModel(
            name='Sale',
            fields=[
            ],
            options={
                'verbose_name': '\u041f\u0440\u043e\u0434\u0430\u0436\u0430',
                'proxy': True,
                'verbose_name_plural': '\u041f\u0440\u043e\u0434\u0430\u0436\u0438',
            },
            bases=('core.ticket',),
        ),
    ]
