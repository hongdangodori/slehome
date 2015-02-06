# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0068_auto_20150201_1937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='1cff987085b0f18e7c8e11f4bd3e8bb198f1db7f2064112d996a2394b3b01f03'),
            preserve_default=True,
        ),
    ]
