# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0036_auto_20150130_0533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='8cfb45aa07d6eedbcc66b17a069e1d2475e9345c20abb6e07122f01004613afc'),
            preserve_default=True,
        ),
    ]
