from django.urls import path,include
from django.conf.urls import url
from assignment.views import view_list_assignment,\
    QuestionView,assignmentCreate,QuestionAdd,\
    view_list_my_assignment,assignment_check,\
    studymaterial_upload,SearchView,result,\
    answersheet,blog_site_list,add_blog_site,view_blog_site,\
    add_blog,blog,QuestionUpdate,AssignmentUpdate,QuestionDelete,\
    index,AssignmentLikeToggle,booklet,my_booklet,\
    index_booklet,index_jee_main,index_jee_adv,index_ssc,index_others,\
    show_submission,filter_search,add_intrest,IntrestDelete,home


app_name='assignment'

urlpatterns = [
    path('',home,name='home'),
    path('index',index,name='index'),
    path('index_jee_main',index_jee_main,name='index_jee_main'),
    path('index_jee_adv',index_jee_adv,name='index_jee_adv'),
    path('index_ssc',index_ssc,name='index_ssc'),
    path('index_others',index_others,name='index_others'),
    path('add_intrest',add_intrest,name='add_intrest'),


    path('all-assignment',view_list_assignment,name='assignment_page'),
    path('myassignment',view_list_my_assignment,name='my_assignment_page'),
    path('myassignment/<pk>',view_list_my_assignment,name='my_assignment_page'),
    path('myassignment_update/<pk>',AssignmentUpdate.as_view(),name='my_assignment_update'),
    path('assignment/add',assignmentCreate,name='assignment_add'),
    path('assignment/<pk>',QuestionView.as_view(),name='assignment'),
    path('assignment-like/<id>',AssignmentLikeToggle,name='like'),
    path('question/add/<pk>',QuestionAdd,name='question_add'),
    path('question/update/<pk>',QuestionUpdate.as_view(),name='question_update'),
    path('question/delete/<pk>',QuestionDelete.as_view(),name='question_delete'),
    path('assignment_check/<int:assignment_id>',assignment_check,name='assignment_check'),
    path('uploadfile/',studymaterial_upload,name='uploadfile'),


    path('search',SearchView.as_view(),name='search'),
    path('filter',filter_search,name='filter'),
    path('delete_intrest/<pk>',IntrestDelete.as_view(),name='delete_intrest'),



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
    path('submissions/<pk>',show_submission,name='show_submission'),

    path('booklet',booklet,name='booklet'),
    path('my-booklet',my_booklet,name='my-booklet'),
    path('my-booklet/<pk>',my_booklet,name='my-booklet'),
    path('index-booklet',index_booklet,name='index_booklet'),



              ]