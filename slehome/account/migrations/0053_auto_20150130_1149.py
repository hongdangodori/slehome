# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0052_auto_20150130_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='2469796ced397d3a5910ba96977dddf51e62f306a7ab069e26bbf7e931aea0fd'),
            preserve_default=True,
        ),
    ]
