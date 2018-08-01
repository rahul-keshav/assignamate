from django.urls import path,include
from django.conf.urls import url
from .views import post,My_post,assignment_discussion,assignment_discussion_reply

app_name='home'

urlpatterns = [
    path('',post,name='home'),
    path('mypost',My_post.as_view(),name='my_post'),
    path('mypost/<pk>',My_post.as_view(),name='my_post'),
    path('assignment-discussion/<pk>',assignment_discussion,name='assignment-discussion'),
    path('assignment-discussion-reply/<pk>',assignment_discussion_reply,name='assignment-discussion-reply'),
]