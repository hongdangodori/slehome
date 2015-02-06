# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0097_auto_20150202_0039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='30c6f2726c1e578da200432a7fc7d6e586b51b7970d06f6f5a1fd6ec0af36551'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
            preserve_default=True,
        ),
    ]
