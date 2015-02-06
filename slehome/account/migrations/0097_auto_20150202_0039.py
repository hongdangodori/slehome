# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0096_auto_20150201_2051'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='3635261e81ece5847f80557667f19c082cb20feb39a3fbaeb31df9b5fe98a104', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(),
            preserve_default=True,
        ),
    ]
