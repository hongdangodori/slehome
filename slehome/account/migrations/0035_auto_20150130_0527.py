# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0034_auto_20150130_0526'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='b58682ace971f4315ce03971949c131ac1025912bec31b9dfa12ffb841f1cc1c'),
            preserve_default=True,
        ),
    ]
