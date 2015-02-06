# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_auto_20150129_1652'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='3b8fd8533eb0fa67609992573cb7ce7e503d42d3b29400e2c1e4069fcd3605ce', max_length=64),
            preserve_default=True,
        ),
    ]
