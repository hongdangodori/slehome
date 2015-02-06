# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0038_auto_20150130_0537'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='3a4869587289507b8c7002ae8c110704f7567fcb903ce21c2b4a6f5f5a279091'),
            preserve_default=True,
        ),
    ]
