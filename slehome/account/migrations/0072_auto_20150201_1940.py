# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0071_auto_20150201_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='2a3694d73b30d33c9a0debc6308812f9ead0e43e60c18b057f2d0ca354322272'),
            preserve_default=True,
        ),
    ]
