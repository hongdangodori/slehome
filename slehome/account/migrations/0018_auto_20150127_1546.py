# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0017_auto_20150126_1749'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='c911faaabfdc0ac06e816ed5cf9e720f18399f7a860663eef60fefa5b41a5dd5', max_length=64),
            preserve_default=True,
        ),
    ]
