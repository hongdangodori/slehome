# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0078_auto_20150201_1955'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='1b207b79bede3f934aebab63701e5747e4319a3b180ad2a6a7c9e83114843348', max_length=64),
            preserve_default=True,
        ),
    ]
