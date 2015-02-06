# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0039_auto_20150130_0540'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='defe930f48000de8ea28d693eafb8cdad5513e5769b789f6017b079e5c16e1ce', max_length=64),
            preserve_default=True,
        ),
    ]
