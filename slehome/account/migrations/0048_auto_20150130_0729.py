# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0047_auto_20150130_0726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='b0af508885f3400dd8f9692ad8c8e83cd1474c62fc32ab8bf2b9bd93c978f343', max_length=64),
            preserve_default=True,
        ),
    ]
