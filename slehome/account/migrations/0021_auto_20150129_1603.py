# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_auto_20150129_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='d7732e87c65eac3429f9da6c6e46cc0cbb6e991fec43bd8035847925319cac5c'),
            preserve_default=True,
        ),
    ]
