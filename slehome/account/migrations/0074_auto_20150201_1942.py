# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0073_auto_20150201_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='7462ae949fa8660646d4c0e4cfe0108d6847de15c4f82a3a243929de911ab7b5'),
            preserve_default=True,
        ),
    ]
