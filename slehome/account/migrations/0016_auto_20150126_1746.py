# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0015_auto_20150126_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='ee4a80d6e3c382f44358001f594599981282c1ec940fd987c22801cd4f3c63d3', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='myuser',
            name='stu_num',
            field=models.CharField(unique=True, max_length=8),
            preserve_default=True,
        ),
    ]
