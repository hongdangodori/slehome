# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0083_auto_20150201_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='4f811716489d07d676b4df8d0f85ebae001dbbe6c0db15df1c0dd5c3c033dd69', max_length=64),
            preserve_default=True,
        ),
    ]
