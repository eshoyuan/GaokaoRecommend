from django.urls import path
from . import views

# 增加了一个url
urlpatterns = [
  path('', views.index, name='index'),
]

urlpatterns = [
    path('welcome.html/', views.welcome, name='welcome'),
]