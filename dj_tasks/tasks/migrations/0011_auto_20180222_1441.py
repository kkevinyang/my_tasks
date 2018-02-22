# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tasks', '0010_biz_sqls_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SQL',
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
        migrations.RemoveField(
            model_name='sqls',
            name='owner',
        ),
        migrations.DeleteModel(
            name='SQLs',
        ),
    ]
