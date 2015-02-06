# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0027_auto_20150129_2018'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='6322a754a9e98b3e6a56fc44739d11b91bb7ad8955c017ba23179ed3bcb8e6e6', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolink',
            name='member_intro',
            field=models.OneToOneField(to='account.MemberIntro'),
            preserve_default=True,
        ),
    ]
