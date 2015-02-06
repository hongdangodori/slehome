# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0086_auto_20150201_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='04210d3e8e12e1fc99a2072b7815181ae94c17ea8948399fe8b42a7195ced7bc', max_length=64),
            preserve_default=True,
        ),
    ]
