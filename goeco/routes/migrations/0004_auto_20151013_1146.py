# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0003_usersettings_car_owner'),
    ]

    operations = [
        migrations.RenameField(
            model_name='goecoaccount',
            old_name='usersettings',
            new_name='user_settings',
        ),
    ]
