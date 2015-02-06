# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0082_auto_20150201_2015'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='5d56513d076dc1ba925f203ec16ad73400a8400916c910ddc809da4d59d41e09'),
            preserve_default=True,
        ),
    ]
