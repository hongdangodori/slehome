# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menulist',
            name='display_ord',
            field=models.IntegerField(max_length=2),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='menulistfornonmembers',
            name='display_ord',
            field=models.IntegerField(max_length=2),
            preserve_default=True,
        ),
    ]
