# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Pentagram', '0006_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]
