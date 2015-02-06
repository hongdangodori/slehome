# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberIntro',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('stat1_name', models.CharField(max_length=15)),
                ('stat2_name', models.CharField(max_length=15)),
                ('stat3_name', models.CharField(max_length=15)),
                ('stat4_name', models.CharField(max_length=15)),
                ('stat1_num', models.IntegerField(max_length=5)),
                ('stat2_num', models.IntegerField(max_length=5)),
                ('stat3_num', models.IntegerField(max_length=5)),
                ('stat4_num', models.IntegerField(max_length=5)),
                ('intro', models.TextField(null=True)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='memberintro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo_link',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('file_name', models.CharField(max_length=20)),
                ('upload_path', models.CharField(max_length=20, default='/home/sle/media/member/')),
                ('member_intro', models.ForeignKey(to='members.MemberIntro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
