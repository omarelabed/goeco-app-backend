# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0004_auto_20151013_1146'),
    ]

    operations = [
        migrations.RenameField(
            model_name='trackpoint',
            old_name='trackPoints',
            new_name='activity',
        ),
    ]
