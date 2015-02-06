# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0059_auto_20150130_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='2e4e66ee8b9db2b3424366ae4303bb6cf15dc1ec141fd9db496379eb71c97e0e', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='member_intro',
            field=models.ForeignKey(to='account.MemberIntro'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='stat_value',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)]),
            preserve_default=True,
        ),
    ]
