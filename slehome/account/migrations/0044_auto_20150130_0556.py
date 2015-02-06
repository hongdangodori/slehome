# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0043_auto_20150130_0555'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='dc727866dcdd1c1f247d87d815ce0deb346fa3a766476475fc50ca761d21184b', max_length=64),
            preserve_default=True,
        ),
    ]
