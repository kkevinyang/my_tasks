# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 03:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_auto_20180207_1053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[(b'open', b'OPEN'), (b'stop', b'STOP'), (b'delete', b'DELETE')], default=b'open', max_length=10),
        ),
    ]
