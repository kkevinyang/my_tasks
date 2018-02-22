from django.conf.urls import url
from . import views

# 这个如果不加的话会报错：django.urls.exceptions.NoReverseMatch: 'blog' is not a registered namespace
app_name = "post"

# 为每一个应用创建单独的urls.py文件是最好的方法，可以保证你的应用能给别的项目再度使用
urlpatterns = [
    url(r'^$', views.main, name='post_list'),
]
