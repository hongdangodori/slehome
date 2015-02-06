# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0055_auto_20150130_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='444a7bc22ce53a4dbf99c9628e3140e98a8ba63164a34c2549e2041288e8aa79'),
            preserve_default=True,
        ),
    ]
