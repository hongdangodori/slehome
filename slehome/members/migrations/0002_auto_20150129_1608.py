# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='memberintro',
            name='user',
        ),
        migrations.RemoveField(
            model_name='photo_link',
            name='member_intro',
        ),
        migrations.DeleteModel(
            name='MemberIntro',
        ),
        migrations.DeleteModel(
            name='Photo_link',
        ),
    ]
