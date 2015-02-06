# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0105_auto_20150203_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='f1905db17440d1aaf3bc2c271045c43817fd4c8a8a840dd216b22d9bce2b018f'),
            preserve_default=True,
        ),
    ]
