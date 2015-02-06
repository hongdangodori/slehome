# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0079_auto_20150201_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='5f9629f140778a73b644a8340f33d8179468df97dd3ac55634707b1239f4cb84'),
            preserve_default=True,
        ),
    ]
