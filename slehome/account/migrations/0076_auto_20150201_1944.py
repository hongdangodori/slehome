# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0075_auto_20150201_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='f861b940f465a5f01776a60f4232c10e1a1a7621379c5ef9fa465273fa758264'),
            preserve_default=True,
        ),
    ]
