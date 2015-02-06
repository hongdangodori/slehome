# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0074_auto_20150201_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='90972972e25ececfd41e652af8b3539f8917f433b786a9799b234fab48199837'),
            preserve_default=True,
        ),
    ]
