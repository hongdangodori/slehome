# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0019_auto_20150129_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='fb224a9a76d69e543c2f5a387d588cf3ca6372d12e672092b8511f82931cda9f', max_length=64),
            preserve_default=True,
        ),
    ]
