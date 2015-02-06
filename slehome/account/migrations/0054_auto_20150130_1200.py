# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0053_auto_20150130_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='2420219831d708f1c99ce61ae1c4fc27d4318426832d708291590b4ceab4ecbd'),
            preserve_default=True,
        ),
    ]
