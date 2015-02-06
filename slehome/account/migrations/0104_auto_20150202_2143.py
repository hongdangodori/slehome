# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0103_auto_20150202_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='4cbab04bd266123b13d1f627ef1997ebe7a8c7be2c42eff16777351490eb5c02'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_name',
            field=models.CharField(max_length=15, default='데헷력'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(default=10, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=False,
        ),
    ]
