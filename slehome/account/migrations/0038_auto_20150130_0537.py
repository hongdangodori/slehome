# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0037_auto_20150130_0536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='d785536cab45de6fef7ba897411084bb19ae058f56f8ce87234bdd64bfdd515b'),
            preserve_default=True,
        ),
    ]
