# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0033_auto_20150130_0501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='c50ae017a4045484a448f788fac502584b2f9d250b8dbe77185d1b398c84f03a'),
            preserve_default=True,
        ),
    ]
