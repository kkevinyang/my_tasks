from django.conf.urls import url
from . import views

urlpatterns = [
    # post views
    url(r'^$', views.task_list),
    # url(r'^tasks/', views.task_list, name='task_list'),
    # url(r'^$/tasks', views.task_list),
]