# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-02-07 02:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='end',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='task',
            name='start',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
