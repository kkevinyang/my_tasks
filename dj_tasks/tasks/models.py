from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


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
    slug = models.SlugField(max_length=250,
                            unique_for_date='publish')
    author = models.ForeignKey(User,
                               related_name='tasks_task')
    body = models.TextField()
    start = models.DateTimeField(default=timezone.now)
    end = models.DateTimeField(default=timezone.now)

    publish = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10,
                              choices=STATUS_CHOICES,
                              default='open')

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.name

