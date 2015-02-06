# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0092_auto_20150201_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='3cebdce86b8879da0c36c09a5e918760fd81849f0b25d2455bfbf9f5c14263dd'),
            preserve_default=True,
        ),
    ]
