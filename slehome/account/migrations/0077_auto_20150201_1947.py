# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0076_auto_20150201_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='8fb8486879d73bcb8ae7f90caa615ab18b076b2d3279b31e44090a964dc1b2f5'),
            preserve_default=True,
        ),
    ]
