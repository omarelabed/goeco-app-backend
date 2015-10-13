# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('activityMoves', models.CharField(max_length=200)),
                ('activityIDSIA', models.CharField(max_length=200)),
                ('activity', models.CharField(max_length=200)),
                ('validated', models.BooleanField()),
                ('startTime', models.DateTimeField(null=True, blank=True)),
                ('endTime', models.DateTimeField(null=True, blank=True)),
                ('duration', models.IntegerField(null=True, blank=True)),
                ('distance', models.IntegerField(null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GoEcoAccount',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Route',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startTime', models.DateTimeField(null=True, blank=True)),
                ('start_time', models.DateTimeField(null=True, blank=True)),
                ('endTime', models.DateTimeField(null=True, blank=True)),
                ('end_time', models.DateTimeField(null=True, blank=True)),
                ('co2', models.PositiveIntegerField(null=True, blank=True)),
                ('energy', models.PositiveIntegerField(null=True, blank=True)),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='RouteAlternative',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('startTime', models.DateTimeField(null=True, blank=True)),
                ('endTime', models.DateTimeField(null=True, blank=True)),
                ('co2', models.PositiveIntegerField(null=True, blank=True)),
                ('energy', models.PositiveIntegerField(null=True, blank=True)),
                ('route', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='routes.Route')),
                ('user', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TrackPoint',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
                ('time', models.DateTimeField()),
                ('trackPoints', models.ForeignKey(to='routes.Activity')),
            ],
        ),
        migrations.CreateModel(
            name='UserSettings',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('notifications', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Week',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('validated', models.BooleanField()),
                ('goeco_account', models.ForeignKey(to='routes.GoEcoAccount')),
            ],
        ),
        migrations.AddField(
            model_name='routealternative',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='routes.Week', null=True),
        ),
        migrations.AddField(
            model_name='route',
            name='week',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='routes.Week', null=True),
        ),
        migrations.AddField(
            model_name='goecoaccount',
            name='usersettings',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, blank=True, to='routes.UserSettings'),
        ),
        migrations.AddField(
            model_name='activity',
            name='route',
            field=models.ForeignKey(to='routes.Route'),
        ),
    ]
