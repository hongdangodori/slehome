# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0041_auto_20150130_0546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='ba660851d0af4f02589261b81d53d644c42c2086acaa99f72379fead2a40cbe8'),
            preserve_default=True,
        ),
    ]
