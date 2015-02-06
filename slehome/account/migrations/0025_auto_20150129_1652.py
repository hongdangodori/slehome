# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0024_auto_20150129_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='8281ee49bd9746d00ae6e3c7b1ef35d89ebdb7086e1987568e451d3c7ac611b3', max_length=64),
            preserve_default=True,
        ),
    ]
