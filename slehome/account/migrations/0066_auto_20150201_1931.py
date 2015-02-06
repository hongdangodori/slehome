# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0065_auto_20150201_1930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='0ea71f1973632c8dd4dcb06d47600806084f26a943603be11e197ff20d891094'),
            preserve_default=True,
        ),
    ]
