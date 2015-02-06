# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0077_auto_20150201_1947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='5344d02b400591a2a4fa4666a94bfd06b1d077a0b61f92f2e707f4044763dde6'),
            preserve_default=True,
        ),
    ]
