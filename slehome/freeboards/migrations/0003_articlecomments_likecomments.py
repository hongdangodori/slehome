# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('freeboards', '0002_likearticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user', models.CharField(max_length=20, blank=True)),
                ('comments', models.TextField(blank=True)),
                ('pub_date', models.DateField(null=True, blank=True)),
                ('like', models.IntegerField(null=True, blank=True)),
                ('article', models.ForeignKey(to='freeboards.FreeBoard')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LikeComments',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, auto_created=True, verbose_name='ID')),
                ('user', models.CharField(max_length=20, blank=True)),
                ('like', models.BooleanField(default=False)),
                ('comments', models.ForeignKey(to='freeboards.ArticleComments')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
