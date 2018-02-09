# -*- coding: UTF-8 -*-
import threading
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler
# from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
# from django.utils import timezone
# from settings import TIME_ZONE


scheduler = None


def new_scheduler():
    global scheduler
    if scheduler and scheduler.running:
        print('*****APScheduler is already started, pid:{}, tid:{}'.format(os.getpid(),
                                                                           threading.current_thread().getName()))
        return scheduler
    scheduler = BackgroundScheduler()
    job = scheduler.add_job(init_func, 'interval', minutes=1)
    print 'job1:', job
    scheduler.start()
    return scheduler


def init_func():
    print time.strftime('%Y-%m-%d %H:%M:%S')


def init_scheduler():
    print '开始初始化scheduler...'
    global scheduler
    # print 'scheduler:', scheduler
    lock = threading.Lock()  # TIP 多线程同步代码
    with lock:
            if scheduler and scheduler.running:
                    print('*****APScheduler is already started, pid:{}, tid:{}'.format(os.getpid(),
                                                                                       threading.current_thread().getName()))
                    return scheduler
            # executors = {
            #         'default': ThreadPoolExecutor(5),  # 线程模式下进程池大小
            #         'processpool': ProcessPoolExecutor(5),  # 进程模式下进程池大小
            # }
            # job_defaults = {
            #         'coalesce': True,  # 如果有几次未执行，条件可以时是否只执行一次
            #         'max_instances': 1,  # 同一个job同一时间最多有几个实例再跑
            # }
            #
            # scheduler = BackgroundScheduler(executors=executors, job_defaults=job_defaults,
            #                                 timezone=timezone(TIME_ZONE))
            scheduler = BackgroundScheduler()
            job = scheduler.add_job(init_func, 'interval', minutes=1)
            print '新增了定时任务:', job
            scheduler.start()
            return scheduler


class StartupMiddleware(object):

    def __init__(self):
        # 启动后台任务APScheduler
        init_scheduler()
        # from django.core.exceptions import MiddlewareNotUsed
        # raise MiddlewareNotUsed  # TIP 抛出此异常，则Django将从 middleware 栈中移出该 middleware，请求就不会经过此middleware

    def process_request(self, request):
        print("*****enter startup middleware")


# scheduler = new_scheduler()
# scheduler = init_scheduler()
