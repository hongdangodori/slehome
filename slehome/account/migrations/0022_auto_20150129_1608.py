# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0021_auto_20150129_1603'),
    ]

    operations = [
        migrations.CreateModel(
            name='MemberIntro',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('stat1_name', models.CharField(max_length=15)),
                ('stat2_name', models.CharField(max_length=15)),
                ('stat3_name', models.CharField(max_length=15)),
                ('stat4_name', models.CharField(max_length=15)),
                ('stat1_num', models.IntegerField(max_length=5)),
                ('stat2_num', models.IntegerField(max_length=5)),
                ('stat3_num', models.IntegerField(max_length=5)),
                ('stat4_num', models.IntegerField(max_length=5)),
                ('intro', models.TextField(null=True)),
                ('user', models.OneToOneField(related_name='memberintro', to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Photo_link',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file_name', models.CharField(max_length=20)),
                ('upload_path', models.CharField(max_length=20, default='/home/sle/media/member/')),
                ('member_intro', models.ForeignKey(to='account.MemberIntro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(max_length=64, default='a945283332b60e2977c345e80bd0af2c9ec4921ea1e635fbb10412f35ce94855'),
            preserve_default=True,
        ),
    ]
