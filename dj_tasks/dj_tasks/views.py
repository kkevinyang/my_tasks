import json
from django.http import HttpResponse


def home(request):
    data = {
        'name': 'yy'
    }
    return HttpResponse(json.dumps(data), content_type="application/json")