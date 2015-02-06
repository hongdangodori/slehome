# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0087_auto_20150201_2026'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='9703427cefb3f9c4780b02d660399fa994f35cde6b82420f40178497d14b6592'),
            preserve_default=True,
        ),
    ]
