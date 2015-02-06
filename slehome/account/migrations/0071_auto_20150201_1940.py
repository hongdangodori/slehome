# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0070_auto_20150201_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='2b372ce56b1f17ea7b14c8bacaaa012f95b8486bd041327b95ca53adeed5369e', max_length=64),
            preserve_default=True,
        ),
    ]
