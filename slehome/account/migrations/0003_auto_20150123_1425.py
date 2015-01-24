# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_auto_20150123_1400'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='bba1c27a688c31238bf0eec82e82aebba6e7cd3d199756576cad9415affd4dad', max_length=64),
            preserve_default=True,
        ),
    ]
