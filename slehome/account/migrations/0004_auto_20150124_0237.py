# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20150123_1425'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='58318fb25a0b3bd3369842b513bc04b448265bf8f97d761d4efcd775b3c2d3fa', max_length=64),
            preserve_default=True,
        ),
    ]
