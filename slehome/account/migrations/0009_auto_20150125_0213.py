# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0008_auto_20150125_0036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='784a7c1a8af6a973826bf65237bc7f7299b4a1222e8fb4bb274c876eeb31620c'),
            preserve_default=True,
        ),
    ]
