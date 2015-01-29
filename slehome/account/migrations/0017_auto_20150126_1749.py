# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_auto_20150126_1746'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='9456556d8ad71abd1fbb1b3f4d2707b51caa9007df9852165a040d326c2e5d1a'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='birthday',
            field=models.CharField(max_length=6),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='stu_num',
            field=models.IntegerField(max_length=8, unique=True),
            preserve_default=True,
        ),
    ]
