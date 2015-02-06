# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0060_auto_20150130_1750'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='031910ad27f4d5c4ffa8ec23fe5ce895d59611079de70db9c7597121bfc2c443', max_length=64),
            preserve_default=True,
        ),
    ]
