# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0101_auto_20150202_2126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='f961783a970c750b9c0db832dab42b896f0ec7bcff0b0b4725cde205a735b829', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_name',
            field=models.CharField(null=True, max_length=15),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True),
            preserve_default=True,
        ),
    ]
