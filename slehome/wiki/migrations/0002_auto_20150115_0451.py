# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filepath',
            old_name='file_path',
            new_name='file_name',
        ),
        migrations.RemoveField(
            model_name='filepath',
            name='page',
        ),
        migrations.AddField(
            model_name='filepath',
            name='page_name',
            field=models.CharField(max_length=20, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='filepath',
            name='upload_path',
            field=models.CharField(max_length=30, default='/home/sle/upload/'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='page',
            name='new_version',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
