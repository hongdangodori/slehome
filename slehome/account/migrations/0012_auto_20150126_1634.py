# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_auto_20150126_1618'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basicmemberinformation',
            old_name='has_auth_key',
            new_name='gave_auth_key',
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='ffcd87f80648341a15d9b53177aa36b54d6a6e194ac03060606446f763cbb0a2'),
            preserve_default=True,
        ),
    ]
