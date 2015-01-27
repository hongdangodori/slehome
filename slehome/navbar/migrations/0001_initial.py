# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MenuList',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('menu', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=70)),
                ('display_ord', models.IntegerField(max_length=2, unique=True)),
                ('display', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='MenuListForNonmembers',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('menu', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=70)),
                ('display_ord', models.IntegerField(max_length=2, unique=True)),
                ('display', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('num', models.IntegerField(default=0, max_length=2, unique=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
