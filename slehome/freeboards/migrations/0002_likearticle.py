# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeboards', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LikeArticle',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20)),
                ('like', models.BooleanField(default=0)),
                ('article', models.ForeignKey(to='freeboards.FreeBoard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
