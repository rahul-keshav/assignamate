from django.urls import path,include
from assignment.views import view_list_assignment,\
    QuestionView,AssignmentCreate,QuestionAdd,\
    view_list_my_assignment,assignment_check,\
    studymaterial_upload,SearchView,result,\
    answersheet,blog_site_list,add_blog_site,view_blog_site,\
    add_blog,blog,QuestionUpdate,AssignmentUpdate,QuestionDelete,\
    index,AssignmentLikeToggle,studymaterial



app_name='assignment'

urlpatterns = [
    #path('',AssignmentView.as_view(),name='assignment_page'),
    path('',view_list_assignment,name='assignment_page'),
    path('myassignment',view_list_my_assignment,name='my_assignment_page'),
    path('myassignment/<pk>',view_list_my_assignment,name='my_assignment_page'),
    path('myassignment_update/<pk>',AssignmentUpdate.as_view(),name='my_assignment_update'),
    path('assignment/add',AssignmentCreate.as_view(),name='assignment_add'),
    path('assignment/<pk>',QuestionView.as_view(),name='assignment'),
    path('assignment-like/<id>',AssignmentLikeToggle,name='like'),
    path('question/add/<pk>',QuestionAdd,name='question_add'),
    path('question/update/<pk>',QuestionUpdate.as_view(),name='question_update'),
    path('question/delete/<pk>',QuestionDelete.as_view(),name='question_delete'),
    path('assignment_check/<int:assignment_id>',assignment_check,name='assignment_check'),
    path('uploadfile/',studymaterial_upload,name='uploadfile'),
    path('search',SearchView.as_view(),name='search'),
    path('blog_site_list',blog_site_list,name='blog_site_list'),
    path('blog_site_list/<pk>',blog_site_list,name='blog_site_list'),

    path('blog_site/<pk>',view_blog_site,name='blog_site'),

    path('create_blog_site',add_blog_site,name='add_blog_site'),
    # path('my_blog_site_list',blog_site_list,name='blog_site'),
    # path('blog_site_list/<pk>',blog_site_list,name='blog_site'),

    path('blog/<pk>',blog,name='blog'),
    path('add_blog/<pk>',add_blog,name='add_blog'),

    path('result',result,name='result'),
    path('answersheet/<ass_id>-<ans_id>',answersheet,name='answersheet'),
    path('index',index,name='index'),
    path('studymaterial',studymaterial,name='studymaterial'),

              ]