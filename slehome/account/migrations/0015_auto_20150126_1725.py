# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0014_auto_20150126_1635'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='birthday',
            field=models.IntegerField(default=950225, max_length=6),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='21030fd3c6537284c6a6479dd82643ecbababe36738a6801f7467159221e211d', max_length=64),
            preserve_default=True,
        ),
    ]
