# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('routes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reason',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=200)),
                ('label', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='route',
            name='reason',
            field=models.ForeignKey(to='routes.Reason', null=True),
        ),
        migrations.AddField(
            model_name='routealternative',
            name='reason',
            field=models.ForeignKey(to='routes.Reason', null=True),
        ),
    ]
