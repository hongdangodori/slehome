# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0013_auto_20150126_1635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='91ca2980268751e7da71e41721abd73edee753d2c25576bbfc63d51f05d15649'),
            preserve_default=True,
        ),
    ]
