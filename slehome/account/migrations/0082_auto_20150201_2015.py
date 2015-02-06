# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0081_auto_20150201_2002'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='d4ceca61e4f90a10f18accafcc54a260a4c8fce05be1d1174116662fd8b873cf'),
            preserve_default=True,
        ),
    ]
