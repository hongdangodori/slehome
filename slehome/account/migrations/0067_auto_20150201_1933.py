# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0066_auto_20150201_1931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='0bcb237ff694a46fdd3537e2216c2eb361ea8f98ae2897ff99fc9a9536292377'),
            preserve_default=True,
        ),
    ]
