# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0012_auto_20180222_1442'),
    ]

    operations = [
        migrations.AddField(
            model_name='sql',
            name='type',
            field=models.CharField(verbose_name='SQL类型', max_length=10, default='3', choices=[('1', '依赖表(第一层)'), ('2', '中间表(第二层)'), ('3', '指标(第三层)')]),
        ),
        migrations.AlterField(
            model_name='biz',
            name='biz_name',
            field=models.CharField(verbose_name='业务线名称', max_length=250),
        ),
        migrations.AlterField(
            model_name='biz',
            name='description',
            field=models.TextField(verbose_name='业务线简介', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sql',
            name='body',
            field=models.TextField(verbose_name='SQL内容'),
        ),
        migrations.AlterField(
            model_name='sql',
            name='owner',
            field=models.ForeignKey(verbose_name='创建人', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sql',
            name='test_sql_name',
            field=models.CharField(verbose_name='SQL名称', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='body',
            field=models.TextField(verbose_name='要跑的SQL'),
        ),
        migrations.AlterField(
            model_name='task',
            name='end',
            field=models.DateTimeField(verbose_name='结束时间', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='name',
            field=models.CharField(verbose_name='任务名称', max_length=250),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.ForeignKey(verbose_name='创建人', blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(verbose_name='开始时间', default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(verbose_name='任务状态', max_length=10, default='open', choices=[('open', 'OPEN'), ('stop', 'STOP'), ('delete', 'DELETE')]),
        ),
        migrations.AlterField(
            model_name='type',
            name='type_name',
            field=models.CharField(verbose_name='类型名称', max_length=250),
        ),
    ]
