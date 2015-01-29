# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20150126_1634'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicmemberinformation',
            name='generated_account',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='be7ae226ea973bd08c3d29059c704f38c17989a35b9d0078d67fc643f075a43d', max_length=64),
            preserve_default=True,
        ),
    ]
