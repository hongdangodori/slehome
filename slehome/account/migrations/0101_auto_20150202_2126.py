# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0100_auto_20150202_2123'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='eebb2c3afdbe7ac4c09d7ef6c757b948a6d37a0adf8b8e37ba9b2cb3df284645'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_name',
            field=models.CharField(max_length=15, default='데헷'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=10),
            preserve_default=False,
        ),
    ]
