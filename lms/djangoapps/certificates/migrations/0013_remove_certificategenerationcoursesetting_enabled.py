# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0012_certificategenerationcoursesetting_include_hours_of_effort'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certificategenerationcoursesetting',
            name='enabled',
        ),
    ]
