# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0030_auto_20150130_0215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accountsettingsmenu',
            name='link',
            field=models.CharField(blank=True, max_length=70),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='200b13e43b9313ded80c528c4eda4b0e6a4561fed351fb5417192ca190363b98', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='memberintro',
            name='intro',
            field=models.TextField(),
            preserve_default=True,
        ),
    ]
