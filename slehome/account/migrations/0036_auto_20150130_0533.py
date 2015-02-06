# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0035_auto_20150130_0527'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='51ac8b8bc4da8bdbec8bbc75085d3e590d76c55df8e30df020fcb02a5f99a6a0', max_length=64),
            preserve_default=True,
        ),
    ]
