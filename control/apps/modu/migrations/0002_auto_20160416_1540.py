# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('modu', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PartableModel',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('create_datetime', models.DateTimeField(auto_now_add=True)),
                ('deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(null=True, blank=True)),
                ('file_size', models.FloatField(null=True, blank=True)),
                ('pitch', models.FloatField(default=0)),
                ('azimuth', models.FloatField(default=0)),
                ('antenna_type', models.CharField(max_length=20, choices=[(b'default', 'default'), (b'yagi', 'yagi')])),
                ('channel_type', models.CharField(max_length=20, choices=[(b'default', 'default'), (b'free space loss', 'free space loss')])),
            ],
            options={
                'db_table': 'partable',
            },
        ),
        migrations.AlterField(
            model_name='distrimodel',
            name='distri_mode',
            field=models.CharField(max_length=20, choices=[(b'default', 'default'), (b'random', 'infact'), (b'uniform', 'uniform')]),
        ),
        migrations.AddField(
            model_name='partablemodel',
            name='distri',
            field=models.ForeignKey(to='modu.DistriModel', on_delete=django.db.models.deletion.PROTECT),
        ),
    ]
