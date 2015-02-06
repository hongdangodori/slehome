# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0058_auto_20150130_1320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='a9161de64fc89b9daa5dd408d93974e14600f37cf46127b9843130224b7bb0a0'),
            preserve_default=True,
        ),
    ]
