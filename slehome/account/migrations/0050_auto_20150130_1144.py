# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0049_auto_20150130_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='8e6352982a9a96d110d0d8b8ff3299ac8df2ad85433360d83928cdb486dce225'),
            preserve_default=True,
        ),
    ]
