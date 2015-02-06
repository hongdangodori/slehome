# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0099_auto_20150202_0523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='7ae5b95c3d6a7694e3eafa69ed538eaf41900045a55a2a914d7831680fedd9fa', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_name',
            field=models.CharField(max_length=15, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=True,
        ),
    ]
