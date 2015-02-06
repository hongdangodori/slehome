# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0067_auto_20150201_1933'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='882d73288b55208de4b674c5dc3d995afb7b9281acd6943216a7f62fb1d3ddf0'),
            preserve_default=True,
        ),
    ]
