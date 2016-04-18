# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modu', '0003_timetablemodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='SignalModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('file_size', models.FloatField(null=True, blank=True)),
                ('snr', models.IntegerField()),
                ('timetable', models.ForeignKey(to='modu.TimetableModel', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'db_table': 'signal',
            },
        ),
    ]
