# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FreeBoard',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(blank=True, max_length=20)),
                ('category', models.CharField(blank=True, max_length=30)),
                ('title', models.CharField(blank=True, max_length=50)),
                ('contents', models.TextField(blank=True)),
                ('pub_date', models.DateField(null=True, blank=True)),
                ('hits', models.IntegerField(null=True, blank=True)),
                ('file_path', models.CharField(null=True, blank=True, max_length=50)),
                ('like', models.IntegerField(null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
