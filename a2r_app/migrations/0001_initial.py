# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EdgeCase',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('invalid', models.CharField(max_length=5)),
                ('valid', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='PurePower',
            fields=[
                ('power', models.IntegerField(serialize=False, primary_key=True)),
                ('roman_rep', models.CharField(max_length=1)),
            ],
        ),
    ]
