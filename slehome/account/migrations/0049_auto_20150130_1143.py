# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0048_auto_20150130_0729'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='78558c9915707c7d65f2f7428b465851436dbae2fbf4875228c209fa66a1789b'),
            preserve_default=True,
        ),
    ]
