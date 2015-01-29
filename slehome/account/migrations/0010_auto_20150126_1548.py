# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0009_auto_20150125_0213'),
    ]

    operations = [
        migrations.AddField(
            model_name='basicmemberinformation',
            name='completed_validation',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='gave_auth_key',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='3c1562074178f6c4dd0b72d31c3a45343d60f839b9a30795e4dc8c6a61175c41', max_length=64),
            preserve_default=True,
        ),
    ]
