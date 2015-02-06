# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0057_auto_20150130_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='f4d02a7b3a72426706537a540748afe1f093557d4167b1d64bcd1105b27cc77c'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolink',
            name='file_name',
            field=models.CharField(max_length=64),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='photolink',
            name='upload_path',
            field=models.CharField(max_length=64, default='/home/sle/media/member/'),
            preserve_default=True,
        ),
    ]
