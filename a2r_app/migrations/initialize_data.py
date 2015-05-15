# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


def populate_tables(apps, schema_editor):
    PurePower = apps.get_model('a2r_app', 'PurePower')
    for pwr, rep in settings.PURE_POWERS.iteritems():
        pp = PurePower(power=pwr, roman_rep=rep)
        pp.save()

    EdgeCase = apps.get_model('a2r_app', 'EdgeCase')
    for k, v in settings.EDGE_CASES.iteritems():
        ec = EdgeCase(invalid=k, valid=v)
        ec.save()


class Migration(migrations.Migration):

    dependencies = [
        ('a2r_app', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(populate_tables),
    ]
