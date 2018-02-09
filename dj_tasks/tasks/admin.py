# -*- coding: UTF-8 -*-

import pdb

from django.contrib import admin
from .models import Task
# from dj_tasks.scheduler import scheduler
# from dj_tasks.urls import scheduler
from globals.scheduler import scheduler

print 'get scheduler:', scheduler


def add_task(sql_body):
    print 'sql_body:', sql_body


class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'author', 'publish',
                    'status', 'start', 'end')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('name', 'body')
    prepopulated_fields = {'slug': ('name',)}
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']  # 可排序方式

    def change_view(self, request, object_id, form_url='', extra_context=None):
        # global scheduler
        sql_body = request.POST.get('body')
        if sql_body:
            print 'sql_body:', sql_body
            job = scheduler.add_job(add_task, 'interval', minutes=1, args=[sql_body])
            print 'job3:', job
        return super(TaskAdmin, self).change_view(request, object_id,
                                                     form_url, extra_context=extra_context)

    # def change_view(self, request, object_id, form_url='', extra_context=None):
    #     print request
    #     print object_id
    #     result = super(TaskAdmin, self).change_view(request, object_id, extra_context)
    #     print result
    #
    #     task = Task.objects.get(id__exact=object_id)
    #
    #     if not request.POST.has_key('_addanother') and not request.POST.has_key('_continue'):
    #         result['Location'] = task.get_absolute_url()
    #         return result


admin.site.register(Task, TaskAdmin)
