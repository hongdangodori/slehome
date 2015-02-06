# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0063_auto_20150201_1921'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='ff58b2b37746118d6a26dd123a6bd04d70b73b25caf4322bf26dbe3777d9d52e', max_length=64),
            preserve_default=True,
        ),
    ]
