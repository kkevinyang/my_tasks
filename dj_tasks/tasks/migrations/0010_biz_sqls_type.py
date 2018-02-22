# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0009_remove_task_slug'),
    ]

    operations = [
        migrations.CreateModel(
            name='Biz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('biz_name', models.CharField(max_length=250)),
                ('description', models.TextField(verbose_name='业务简介')),
                ('inserttime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SQLs',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('test_sql_name', models.CharField(max_length=250)),
                ('body', models.TextField()),
                ('description', models.TextField()),
                ('inserttime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('type_name', models.CharField(max_length=250)),
                ('description', models.TextField(verbose_name='类型简介')),
                ('inserttime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=False)),
            ],
        ),
    ]
