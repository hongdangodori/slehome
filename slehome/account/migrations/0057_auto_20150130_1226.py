# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0056_auto_20150130_1207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stat',
            old_name='stat_num',
            new_name='stat_value',
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='47d423b24b4c5f7fd78e71f3878e5c96c4ce9b9a7773ca882ac6d87c34dc4362', max_length=64),
            preserve_default=True,
        ),
    ]
