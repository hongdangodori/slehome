# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0094_auto_20150201_2045'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='AccountSettingsMenu',
            new_name='AccountSettingsMenuList',
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='a231ec47887569a228cd4dc1916711b30974eb92b68456e68befbed89665b2f2'),
            preserve_default=True,
        ),
    ]
