import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Task
from django.core import serializers

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import pdb


def task_list(request):
    paginator = Paginator(Task, 3)
    print(222)
    data = Task.objects.all()
    print(333)
    print(data)
    res = serializers.serialize('json', data)
    print(444)

    # page = request.GET.get('page') or 1
    # try:
    #     posts = paginator.page(page)
    # except PageNotAnInteger:
    #     # If page is not an integer deliver the first page
    #     posts = paginator.page(1)
    # except EmptyPage:
    #     # If page is out of range deliver last page of results
    #     posts = paginator.page(paginator.num_pages)
    # print(333)

    return HttpResponse(res, content_type="application/json")

