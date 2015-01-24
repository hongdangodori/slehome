# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='a3230da72ab0e98cc099f8430ad0858ffeb5d81ddc72b1bdfe31b714b76958ae', max_length=64),
            preserve_default=True,
        ),
    ]
