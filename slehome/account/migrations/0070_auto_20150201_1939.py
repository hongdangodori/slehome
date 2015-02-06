# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0069_auto_20150201_1938'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='b642894f34f4156de7b06c455012e1a40e0b3ae31d04a76fe5f7f76d5e78f15f'),
            preserve_default=True,
        ),
    ]
