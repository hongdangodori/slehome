# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0032_auto_20150130_0242'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='8a230b1acc09def6649c4623da9a1e082ce94695f4c284707d6541718a972e7c', max_length=64),
            preserve_default=True,
        ),
    ]
