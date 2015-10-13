# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0002_auto_20151013_1140'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersettings',
            name='car_owner',
            field=models.BooleanField(default=False),
        ),
    ]
