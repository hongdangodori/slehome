# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0062_auto_20150201_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='51f7c2e2ff389bde7ac03028f149656cc4d187097959ad544c81d31a7d827775', max_length=64),
            preserve_default=True,
        ),
    ]
