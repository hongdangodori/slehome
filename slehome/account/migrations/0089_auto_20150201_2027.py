# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0088_auto_20150201_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='6e2c2c6107b1dc56b44195bf6339885dbea8aee632aa6e8770107bd1ff68ed0f'),
            preserve_default=True,
        ),
    ]
