# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0080_auto_20150201_1959'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='324e7de7d0b0dd383ebccd23d44ccea7c60a40454b589d1a6fe1df0bf57a16c9', max_length=64),
            preserve_default=True,
        ),
    ]
