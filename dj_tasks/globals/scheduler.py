# -*- coding: UTF-8 -*-

import threading
import os
import time
from apscheduler.schedulers.background import BackgroundScheduler


scheduler = None


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

            scheduler = BackgroundScheduler()
            # job = scheduler.add_job(init_func, 'interval', minutes=1)
            # print '新增了定时任务:', job
            scheduler.start()
            return scheduler


scheduler = init_scheduler()
