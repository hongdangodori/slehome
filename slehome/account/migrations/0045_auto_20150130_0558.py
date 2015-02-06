# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0044_auto_20150130_0556'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='e49f139200080ea03a90580e932e3eabb7c9732327371958cc4b9f29105a86d9'),
            preserve_default=True,
        ),
    ]
