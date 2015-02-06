# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0045_auto_20150130_0558'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='43f9a685bc7146b4ecc63bdf9bc3e5136b7543f436a42e4a2f2ae749ffb0c6db', max_length=64),
            preserve_default=True,
        ),
    ]
