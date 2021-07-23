from django.urls import path
from . import views
from django.conf.urls import url

# 增加了一个url
# 设置了默认视图为首页
urlpatterns = [
    path('results.html/', views.results),
    path('welcome.html/', views.welcome),
    path('welcome.html/output', views.new_page),
    path('', views.new_page),  # 返回历年录取数据
]
