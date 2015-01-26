# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20150124_0237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='49473d251787a13567c2ead298dfbdb0404454ecd229b695ae66472720f4beaf', max_length=64),
            preserve_default=True,
        ),
    ]
