# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0104_auto_20150202_2143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='6b498e2d0da2372e5d57a3c764fc3a270bf99ae089fc5108097f4bc2bcd875e5'),
            preserve_default=True,
        ),
    ]
