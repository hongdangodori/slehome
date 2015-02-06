# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('freeboards', '0005_merge'),
    ]

    operations = [
        migrations.CreateModel(
            name='FreeBoards',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('category', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('contents', models.TextField(blank=True)),
                ('pub_date', models.DateField(blank=True, null=True)),
                ('hits', models.IntegerField(blank=True, null=True)),
                ('file_path', models.CharField(blank=True, max_length=50, null=True)),
                ('like', models.IntegerField(blank=True, null=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LikeArticles',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, verbose_name='ID', serialize=False)),
                ('like', models.BooleanField(default=False)),
                ('article', models.ForeignKey(to='freeboards.FreeBoards')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='likearticle',
            name='article',
        ),
        migrations.DeleteModel(
            name='LikeArticle',
        ),
        migrations.RemoveField(
            model_name='likecomments',
            name='comments',
        ),
        migrations.AlterField(
            model_name='articlecomments',
            name='article',
            field=models.ForeignKey(to='freeboards.FreeBoards'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='FreeBoard',
        ),
        migrations.AlterField(
            model_name='likecomments',
            name='user',
            field=models.ForeignKey(to=settings.AUTH_USER_MODEL),
            preserve_default=True,
        ),
    ]
