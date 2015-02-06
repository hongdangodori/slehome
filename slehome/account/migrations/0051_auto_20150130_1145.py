# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0050_auto_20150130_1144'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='6789b1d36b50add9b9e326d2b50ffd43b93a55f2c91d402d9c8aab32677967bd'),
            preserve_default=True,
        ),
    ]
