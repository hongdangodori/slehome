# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeboards', '0003_articlecomments_likecomments'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecomments',
            name='target',
            field=models.IntegerField(blank=True, null=True),
            preserve_default=True,
        ),
    ]
