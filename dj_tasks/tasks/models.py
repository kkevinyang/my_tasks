# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.exceptions import ValidationError


class SQL(models.Model):
    test_sql_name = models.CharField(max_length=250, verbose_name='SQL名称')
    owner = models.ForeignKey(User, verbose_name='创建人', null=True, blank=True)
    body = models.TextField(verbose_name='SQL内容')
    description = models.TextField(verbose_name='SQL简介', null=True, blank=True)
    inserttime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=False)


class Metric(models.Model):
    metric_name = models.CharField(max_length=250, verbose_name='指标名称')
    owner = models.ForeignKey(User, verbose_name='创建人', null=True, blank=True)
    body = models.TextField(verbose_name='指标的SQL内容')
    description = models.TextField(verbose_name='指标简介', null=True, blank=True)
    inserttime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=False)

    def __str__(self):
        return self.metric_name


class Biz(models.Model):
    biz_name = models.CharField(max_length=250, verbose_name='业务线名称')
    description = models.TextField(verbose_name='业务线简介', null=True, blank=True)
    inserttime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=False)


class Type(models.Model):
    type_name = models.CharField(max_length=250, verbose_name='类型名称')
    description = models.TextField(verbose_name='类型简介', null=True, blank=True)
    inserttime = models.DateTimeField(default=timezone.now)
    updatetime = models.DateTimeField(auto_now=True)
    isactive = models.BooleanField(default=False)


class Task(models.Model):
    STATUS_CHOICES = (
        ('open', 'OPEN'),
        ('stop', 'STOP'),
        ('delete', 'DELETE'),
    )
    name = models.CharField(max_length=250, verbose_name='任务名称')
    # slug = models.SlugField(max_length=250,
    #                         unique_for_date='publish')
    owner = models.ForeignKey(User, verbose_name='创建人', null=True, blank=True)
    body = models.TextField(verbose_name='要跑的SQL')
    start = models.DateTimeField(default=timezone.now, verbose_name='开始时间')
    end = models.DateTimeField(default=timezone.now, verbose_name='结束时间')
    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='open', verbose_name='任务状态')
    metric = models.ManyToManyField(Metric, verbose_name='指标', null=True, blank=True)

    def colored_status(self):
        """增加需要渲染颜色的字段"""
        if self.status == 'open':
            color_code = 'green'
        else:
            color_code = 'red'
        # print('color_code:', color_code)
        return format_html(
            '<p style="color: {}">{}</p>',
            color_code,
            self.status,
        )

    colored_status.short_description = u'状态'

    def save(self, *args, **kwargs):
        """重写model的save()"""
        # print('save...')
        super(Task, self).save(*args, **kwargs)  # Call the "real" save() method.

    def clean(self):
        # print('clean...')
        # print('body:', len(self.body))
        self.body = self.body.strip()
        if len(self.body) < 1:
            raise ValidationError('the sql is too short')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name
