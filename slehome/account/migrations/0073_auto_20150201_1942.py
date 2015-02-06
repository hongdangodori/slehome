# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0072_auto_20150201_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='11b7a79dc7f6f589254ae6249d77f3ff26e522d81480c4827f479f4bf672747a'),
            preserve_default=True,
        ),
    ]
