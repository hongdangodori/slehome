# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0090_auto_20150201_2028'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='20fc9e761aef30824a506fc42ddba452a33bc78b9efc7f4e3c8bd6c9d3e2767b', max_length=64),
            preserve_default=True,
        ),
    ]
