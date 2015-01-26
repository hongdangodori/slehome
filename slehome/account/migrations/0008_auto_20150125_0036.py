# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20150124_2357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='032041e35062e26af5461bea51ce4357c7badadd35d97d1acc39fcab0d3e1d5d'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='stu_num',
            field=models.IntegerField(max_length=8),
            preserve_default=True,
        ),
    ]
