# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=250)),
                ('slug', models.SlugField(max_length=250, unique_for_date=b'publish')),
                ('body', models.TextField()),
                ('publish', models.DateTimeField(default=django.utils.timezone.now)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(default=b'todo', max_length=10, choices=[(b'running', b'RUNNING'), (b'stop', b'STOP'), (b'todo', b'TODO'), (b'done', b'DONE')])),
                ('author', models.ForeignKey(related_name='tasks_task', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-publish',),
            },
        ),
    ]
