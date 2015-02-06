# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0028_auto_20150129_2028'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='level',
            field=models.IntegerField(default=1),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='myuser',
            name='point',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='e8bbe0587fbd28fcb1f1b1d8ca43a28a517c59664f6810d6203835c4475471bf'),
            preserve_default=True,
        ),
    ]
