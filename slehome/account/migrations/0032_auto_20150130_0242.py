# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0031_auto_20150130_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='4649c9f99668bc7db28dc048de254551c6360f10cd1a3b6eb6c9ab2676a31acf', max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolink',
            name='member_intro',
            field=models.OneToOneField(to='account.MemberIntro', related_name='photolink'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='stat',
            name='member_intro',
            field=models.ForeignKey(to='account.MemberIntro', related_name='stat'),
            preserve_default=True,
        ),
    ]
