from django.conf.urls import include, url
from django.contrib import admin


urlpatterns = [
    # Examples:
    # url(r'^$', 'dj_tasks.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^jet/', include('jet.urls', 'jet')),  # Django JET URLS
    # url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),  # Django JET dashboard URLS
    url(r'^admin/', include(admin.site.urls)),
]

# from scheduler import StartupMiddleware, new_scheduler
# StartupMiddleware()
#
# scheduler = new_scheduler()
