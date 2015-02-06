# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0098_auto_20150202_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='9a26035d7099b9a0fe43b63ad811139b0e2147bc7922158d42bdb19c965ce654'),
            preserve_default=True,
        ),
    ]
