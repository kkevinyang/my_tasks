from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    # Examples:
    # url(r'^$', include('app.urls', namespace="blog")),
    url(r'^$', TemplateView.as_view(template_name="index.html")),
    url(r'home', views.home),
    url(r'^tasks/', include('tasks.urls')),

    # url(r'^blog/', include('blog.urls')),
    url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', include(admin.site.urls)),
]

# from scheduler import StartupMiddleware, new_scheduler
# StartupMiddleware()
#
# scheduler = new_scheduler()
