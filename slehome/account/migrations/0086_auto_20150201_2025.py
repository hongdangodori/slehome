# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0085_auto_20150201_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='2f7be28e4b07377eb763155f462ee928dbed019ac2d1b31ebcbfdc108c050980'),
            preserve_default=True,
        ),
    ]
