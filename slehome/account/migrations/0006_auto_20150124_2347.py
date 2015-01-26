# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20150124_1859'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='fcef40afc32d0a1c50656053f99a2ac5246332fcf2e95849f48727f349e7d802'),
            preserve_default=True,
        ),
    ]
