# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0091_auto_20150201_2029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='d4c121842dff990b336a7a74438d1093449cd1e11c6faa15d7f39e17f11c9acf', max_length=64),
            preserve_default=True,
        ),
    ]
