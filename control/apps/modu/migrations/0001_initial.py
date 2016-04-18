# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='DistriModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('file_size', models.FloatField(null=True, blank=True)),
                ('distri_id', models.CharField(unique=True, max_length=20)),
                ('distri_lon', models.FloatField(default=0)),
                ('distri_lat', models.FloatField(default=0)),
                ('distri_height', models.IntegerField(default=0)),
                ('distri_ves_num', models.IntegerField(default=0)),
                ('distri_mode', models.CharField(max_length=20, choices=[(b'default', 'default'), (b'random', 'random'), (b'uniform', 'uniform')])),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=django.db.models.deletion.PROTECT)),
            ],
            options={
                'db_table': 'distri',
            },
        ),
    ]
