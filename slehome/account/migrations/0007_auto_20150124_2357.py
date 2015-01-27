# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_auto_20150124_2347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='f26e2ff059e1c71478e358c3f6eb407f217bd163e39fc1b7ab7a53c10c918989', max_length=64),
            preserve_default=True,
        ),
    ]
