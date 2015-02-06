# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0046_auto_20150130_0600'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='ec73e1d7738294ebc8342ab1dee699e6060bbd03993448dc1576ddbfe96377e6', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='nickname',
            field=models.CharField(unique=True, max_length=10),
            preserve_default=True,
        ),
    ]
