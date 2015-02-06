# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0084_auto_20150201_2017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='6e32cbb4115c11b7d8c225bf71c64bfe637fc79c59e031013b1e62c27a282e93'),
            preserve_default=True,
        ),
    ]
