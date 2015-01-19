# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0002_auto_20150115_0451'),
    ]

    operations = [
        migrations.AddField(
            model_name='filepath',
            name='dummy_name',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
    ]
