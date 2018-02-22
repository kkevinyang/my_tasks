# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0011_auto_20180222_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='biz',
            name='description',
            field=models.TextField(verbose_name='业务简介', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='sql',
            name='description',
            field=models.TextField(verbose_name='SQL简介', blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='type',
            name='description',
            field=models.TextField(verbose_name='类型简介', blank=True, null=True),
        ),
    ]
