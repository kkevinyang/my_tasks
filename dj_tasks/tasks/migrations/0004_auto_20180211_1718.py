# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_auto_20180207_1116'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='author',
            new_name='owner',
        ),
        migrations.AlterField(
            model_name='task',
            name='slug',
            field=models.SlugField(max_length=250, unique_for_date='publish'),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(max_length=10, default='open', choices=[('open', 'OPEN'), ('stop', 'STOP'), ('delete', 'DELETE')]),
        ),
    ]
