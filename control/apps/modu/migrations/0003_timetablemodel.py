# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modu', '0002_auto_20160416_1540'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimetableModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('file_size', models.FloatField(null=True, blank=True)),
                ('obtime', models.FloatField(default=0)),
                ('protocol', models.CharField(max_length=20, choices=[(b'default', 'default'), (b'SOTDMA', 'SOTDMA')])),
                ('distri', models.ForeignKey(to='modu.DistriModel', on_delete=django.db.models.deletion.PROTECT)),
                ('partable', models.ForeignKey(to='modu.PartableModel', on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'db_table': 'timetable',
            },
        ),
    ]
