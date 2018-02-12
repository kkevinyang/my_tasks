# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0006_auto_20180212_1709'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.CharField(max_length=128, default='anonymous', editable=False),
        ),
    ]
