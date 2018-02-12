# -*- coding: UTF-8 -*-

import pdb

from django.contrib import admin
from .models import Task
# from dj_tasks.scheduler import scheduler
# from dj_tasks.urls import scheduler
from globals.scheduler import scheduler
from django.contrib.auth.models import User

print('get scheduler:', scheduler)


def add_task(sql_body):
    print('sql_body:', sql_body)


class TaskAdmin(admin.ModelAdmin):

    # list_display = ('name', 'owner', 'start', 'end', 'publish', 'colored_status')
    list_display = ('name', 'start', 'end', 'publish', 'colored_status')

    list_filter = ('status', 'created', 'publish', 'owner')
    search_fields = ('name', 'body')
    prepopulated_fields = {'slug': ('name',)}  # prepopulated_fields属性告诉Django通过输入的标题来填充slug字段
    # raw_id_fields = ('owner',)
    date_hierarchy = 'publish'
    ordering = ['status', '-publish']  # 可排序方式

    def get_queryset(self, request):
        """函数作用：使当前登录的用户只能看到自己负责的服务器"""
        print('get_queryset...')

        qs = super(TaskAdmin, self).get_queryset(request)

        if request.user.is_superuser:
            print('is_superuser')
            # qs.list_display = ('name', 'owner', 'start', 'end', 'publish', 'colored_status')
            return qs
        # self.readonly_fields = ('owner',)
        # self.owner = request.user
        print('user:', request.user)
        return qs.filter(owner=User.objects.filter(username=request.user))

    def get_readonly_fields(self, request, obj=None):
        if request.user.is_superuser:
            return ['publish']
        else:
            # return ['publish', 'owner']
            return ['publish']

    def change_view(self, request, object_id, form_url='', extra_context=None):
        """
        覆盖原生函数：修改已经创建的表时才调用
        """
        print('change_view...')

        # def get_readonly_fields(request, obj=None):
        #     """重新定义此函数，限制普通用户所能修改的字段"""
        #     if request.user.is_superuser:
        #         self.readonly_fields = ['publish']
        #     elif hasattr(obj, 'is_sure'):
        #         if obj.is_sure:
        #             self.readonly_fields = ('project_name', 'to_mail', 'data_selected', 'frequency', 'start_date',
        #                                     'end_date')
        #     else:
        #         # pdb.set_trace()
        #         self.owner = User.objects.filter(pk=object_id)
        #         self.readonly_fields = ('publish', 'owner')
        #
        #     return self.readonly_fields
        #
        # change_obj = Task.objects.filter(pk=object_id)
        # print('change_obj:', change_obj)
        # get_readonly_fields(request, obj=change_obj)
        return super(TaskAdmin, self).change_view(request, object_id, form_url, extra_context=extra_context)

    def save_model(self, request, obj, form, change):
        """
        点击保存时调用
        """
        print('save_model...')

        if change:
            # 修改task
            print('save_model--mod')
            pass
        else:
            # 新增task
            print('save_model--add')
            sql_body = request.POST.get('body')
            # obj.owner = request.user.username
            pdb.set_trace()

            # if getattr(obj, 'owner', None) is None:
            #     # obj.owner = request.user.username
            obj.owner = request.user.username

            obj.save()
            # obj.last_modified_by = request.user
            if sql_body:
                print('新增了sql任务:', sql_body)
                job = scheduler.add_job(add_task, 'interval', minutes=1, args=[sql_body])
                print('job4:', job)

        # super(TaskAdmin, self).save_model(request, obj, form, change)

    def add_view(self, request, form_url='', extra_context=None):
        print('add_view...')
        # pdb.set_trace()
        print('request.user:', request.user.username)
        # request.GET.owner = request.user.username
        return super(TaskAdmin, self).add_view(request, form_url, extra_context=extra_context)

    def get_form(self, request, *args, **kwargs):
        print('get_form...')
        form = super(TaskAdmin, self).get_form(request, *args, **kwargs)
        # pdb.set_trace()

        form.owner = request.user
        return form

    # def formfield_for_dbfield(self, db_field, **kwargs):
    #     # print('formfield_for_dbfield...')
    #     print ('db_field:', db_field.name)
    #     field = super(TaskAdmin, self).formfield_for_dbfield(db_field, **kwargs)
    #     # print ('field:', field)
    #     if field:
    #         print ('field.initial:', field.initial)
    #
    #     if db_field.name == 'owner':
    #         field.initial = request.user
    #
    #     return field


admin.site.register(Task, TaskAdmin)
