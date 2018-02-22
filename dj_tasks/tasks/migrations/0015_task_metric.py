# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0014_auto_20180222_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='metric',
            field=models.ForeignKey(verbose_name='指标', blank=True, null=True, to='tasks.Metric'),
        ),
    ]
