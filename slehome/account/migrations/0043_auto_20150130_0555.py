# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0042_auto_20150130_0549'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='9df727b9a6beef54f492e25bf075965388bd6cc5e1f34928fb7677861b10f808'),
            preserve_default=True,
        ),
    ]
