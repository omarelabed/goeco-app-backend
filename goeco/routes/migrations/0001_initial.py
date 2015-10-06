# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('km', models.PositiveIntegerField()),
                ('start_time', models.DateTimeField(verbose_name=b'date published')),
                ('week', models.PositiveIntegerField()),
                ('week_duration', models.PositiveIntegerField()),
                ('co2', models.PositiveIntegerField()),
                ('energy', models.PositiveIntegerField()),
                ('reason', models.CharField(max_length=200)),
                ('status', models.CharField(max_length=200)),
            ],
        ),
    ]
