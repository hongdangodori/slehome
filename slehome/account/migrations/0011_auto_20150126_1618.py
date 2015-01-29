# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_auto_20150126_1548'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='gave_auth_key',
        ),
        migrations.AddField(
            model_name='basicmemberinformation',
            name='has_auth_key',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='234b23c3365fcf4c2e2bbbea9054beb32d7f0400e5bdad73f9c5f2994abf5aac', max_length=64),
            preserve_default=True,
        ),
    ]
