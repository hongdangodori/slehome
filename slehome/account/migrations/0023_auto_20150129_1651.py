# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20150129_1608'),
    ]

    operations = [
        migrations.CreateModel(
            name='Photolink',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('file_name', models.CharField(max_length=20)),
                ('upload_path', models.CharField(default='/home/sle/media/member/', max_length=20)),
                ('member_intro', models.ForeignKey(to='account.MemberIntro')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='photo_link',
            name='member_intro',
        ),
        migrations.DeleteModel(
            name='Photo_link',
        ),
        migrations.AlterField(
            model_name='basicmemberinformation',
            name='auth_key',
            field=models.CharField(default='4dc724db3ad097a8a433340f57e00a40306905adf49a51fe939155e9345f1978', max_length=64),
            preserve_default=True,
        ),
    ]
