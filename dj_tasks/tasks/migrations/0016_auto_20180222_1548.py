# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0015_task_metric'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='metric',
        ),
        migrations.AddField(
            model_name='task',
            name='metric',
            field=models.ManyToManyField(verbose_name='指标', blank=True, null=True, to='tasks.Metric'),
        ),
    ]
