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
            name='BasicMemberInformation',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('stu_num', models.IntegerField(unique=True, max_length=8)),
                ('auth_key', models.CharField(default='f8345f52b1208969186e1f80f386cd22fce4939dd545121f20dbedfff4f43a76', max_length=64)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MyUser',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('fullname', models.CharField(max_length=20)),
                ('nickname', models.CharField(unique=True, max_length=20)),
                ('stu_num', models.IntegerField(unique=True, max_length=8)),
                ('phone_num', models.CharField(max_length=11)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, related_name='myuser')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
