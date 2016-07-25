# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pentagram', '0003_auto_20160715_1023'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='text',
            new_name='comment',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='photo_id',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RemoveField(
            model_name='photo',
            name='counter_Like',
        ),
        migrations.AddField(
            model_name='photo',
            name='counter_like',
            field=models.IntegerField(default=0),
        ),
    ]
