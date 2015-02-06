# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0026_auto_20150129_1653'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountSettingsMenu',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('menu', models.CharField(max_length=20)),
                ('link', models.CharField(max_length=70)),
                ('display_ord', models.IntegerField(max_length=2)),
                ('display', models.BooleanField(default=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('stat_name', models.CharField(max_length=15)),
                ('stat_num', models.IntegerField(max_length=5)),
                ('member_intro', models.ForeignKey(to='account.MemberIntro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat1_name',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat1_num',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat2_name',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat2_num',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat3_name',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat3_num',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat4_name',
        ),
        migrations.RemoveField(
            model_name='memberintro',
            name='stat4_num',
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='84cc742a1ae5a254ddef6b5399d741eb70fee97ced83422952bf9b28d243649e', max_length=64),
            preserve_default=True,
        ),
    ]
