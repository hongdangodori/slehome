# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0029_auto_20150129_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettingsmenu',
            name='link',
            field=models.CharField(max_length=70, null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='7d3edcc53b8043fe0f5dc3cde666ca5baa0e666d5513c7c87426f25e5e1cedcd', max_length=64),
            preserve_default=True,
        ),
    ]
