# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0093_auto_20150201_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='0eba3d45f438d0228de2d9e48fded71f0eabc71863b5b812b3328765bfc1c76f'),
            preserve_default=True,
        ),
    ]
