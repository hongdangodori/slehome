# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_auto_20150129_1651'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='1dfd19e9d1122709d101915863514b008980a5e82699a84bc0cf56994b057fc0', max_length=64),
            preserve_default=True,
        ),
    ]
