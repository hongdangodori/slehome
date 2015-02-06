# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0089_auto_20150201_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='49c5e56846347da9d937e93521a5166adedb1064df921dad985556f9e4301f75'),
            preserve_default=True,
        ),
    ]
