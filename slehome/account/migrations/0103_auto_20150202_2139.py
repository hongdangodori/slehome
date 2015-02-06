# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0102_auto_20150202_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='a9b60a55dc8d492f33f702c46217a1dfc8f8cb11cf269263c9e2eef77593787c', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_name',
            field=models.CharField(blank=True, max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(blank=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], null=True),
            preserve_default=True,
        ),
    ]
