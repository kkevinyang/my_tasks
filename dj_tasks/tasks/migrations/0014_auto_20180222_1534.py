# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0013_auto_20180222_1525'),
    ]

    operations = [
        migrations.CreateModel(
            name='Metric',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('metric_name', models.CharField(verbose_name='指标名称', max_length=250)),
                ('body', models.TextField(verbose_name='指标的SQL内容')),
                ('description', models.TextField(verbose_name='指标简介', blank=True, null=True)),
                ('inserttime', models.DateTimeField(default=django.utils.timezone.now)),
                ('updatetime', models.DateTimeField(auto_now=True)),
                ('isactive', models.BooleanField(default=False)),
                ('owner', models.ForeignKey(verbose_name='创建人', blank=True, null=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='sql',
            name='type',
        ),
    ]
