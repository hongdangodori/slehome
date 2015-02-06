# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0106_auto_20150203_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='5dc29f509c259ba825c4d293ee2b7346457fbee4529f9a13595c4f3faff6ce1a'),
            preserve_default=True,
        ),
    ]
