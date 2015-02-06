# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_filepath_dummy_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='page',
            name='author',
        ),
    ]
