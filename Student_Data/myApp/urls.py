from django.urls import path
from myApp import views

urlpatterns = [
path('', views.home, name="home"),
path('manage', views.manage, name="manage"),
]