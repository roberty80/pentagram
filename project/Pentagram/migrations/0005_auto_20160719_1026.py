# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pentagram', '0004_auto_20160718_1405'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='photo',
            new_name='photo_id',
        ),
    ]
