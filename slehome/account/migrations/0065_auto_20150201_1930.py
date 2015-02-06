# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0064_auto_20150201_1922'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='24d38f74a4573265bffc80d06fa326a607bff6ea265b27d6acc8cb8cfa98c35e'),
            preserve_default=True,
        ),
    ]
