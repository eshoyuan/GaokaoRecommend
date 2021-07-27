from django.urls import path
from . import views
from django.conf.urls import url

# 增加了一个url
# 设置了默认视图为首页
urlpatterns = [
    path('welcome.html/', views.welcome),
    path('news.html/', views.news),
    path('table.html/', views.information),
    path('welcome.html/output', views.new_page),
    path('', views.new_page),  # 返回历年录取数据
    path('welcome.html/test.html/', views.test),
]
