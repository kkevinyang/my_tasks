# -*- coding: UTF-8 -*-

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.core.exceptions import ValidationError


class Task(models.Model):
    # STATUS_CHOICES = (
    #     ('running', 'RUNNING'),
    #     ('stop', 'STOP'),
    #     ('todo', 'TODO'),
    #     ('done', 'DONE'),
    # )

    STATUS_CHOICES = (
        ('open', 'OPEN'),
        ('stop', 'STOP'),
        ('delete', 'DELETE'),
    )

    name = models.CharField(max_length=250)
    # slug = models.SlugField(max_length=250,
    #                         unique_for_date='publish')
    owner = models.ForeignKey(User, null=True, blank=True)
    # owner = models.CharField(default='anonymous', max_length=128, editable=False)
    body = models.TextField()
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='open')

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

