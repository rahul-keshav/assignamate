from django.urls import path,include
from django.conf.urls import url
from . import views

app_name='home'

urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('mypost',views.My_post.as_view(),name='my_post'),
    path('mypost/<pk>',views.My_post.as_view(),name='my_post'),
]