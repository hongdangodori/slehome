# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_auto_20150127_1546'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='e13bc634b840d2831ee61e874e0252b13d7ce8f07bb087d34757268905cd4614'),
            preserve_default=True,
        ),
    ]
