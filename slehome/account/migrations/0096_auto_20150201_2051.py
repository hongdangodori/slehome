# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0095_auto_20150201_2050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='3a59b7697feedae8730db6d97c9e51e5b928c8cc03d1b8cd9b3e2a3517010bcd'),
            preserve_default=True,
        ),
    ]
