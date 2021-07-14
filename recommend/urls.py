from django.urls import path
from . import views
from django.conf.urls import url
# 增加了一个url
# 设置了默认视图为首页
urlpatterns = [
    url(r'^$', views.welcome),
    path('welcome.html/', views.welcome, name='welcome'),
]