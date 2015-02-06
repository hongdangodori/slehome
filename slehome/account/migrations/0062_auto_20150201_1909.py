# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0061_auto_20150201_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='d961ea27644a4065f2ca171b51b980c0998ce61fd6b44470067f3c7f312390a9', max_length=64),
            preserve_default=True,
        ),
    ]
