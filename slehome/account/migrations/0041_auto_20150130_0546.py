# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0040_auto_20150130_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='70ceacff1002aab5131d2bf910c367af6a460df1af1b78005a9cce88fcaa35a6'),
            preserve_default=True,
        ),
    ]
