# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0051_auto_20150130_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='17e6e879a124e82aabec03d929cf0321a3d85672a8ee06c76765f9f27980ab26'),
            preserve_default=True,
        ),
    ]
