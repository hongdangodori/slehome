# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0054_auto_20150130_1200'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='74dfed1ee93d16f22aa635c5f3c631802d99a07bbe2ea5a9f9c3e875935693f5', max_length=64),
            preserve_default=True,
        ),
    ]
