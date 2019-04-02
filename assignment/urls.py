from django.urls import path,include
from django.conf.urls import url
from assignment.views import view_list_assignment,\
    QuestionView,assignmentCreate,QuestionAdd,\
    view_list_my_assignment,assignment_check, \
    booklet_upload,SearchView,result,\
    answersheet,view_workbook_list,add_workbook,view_workbook,\
    add_workbook_page,view_workbook_page,QuestionUpdate,AssignmentUpdate,AssignmentDelete,QuestionDelete,\
    index,AssignmentLikeToggle,booklet,my_booklet,\
    index_booklet,index_jee_main,index_jee_adv,index_ssc,index_others,\
    show_submission,filter_search,add_interest,InterestDelete,\
    home,booklet_preview,BookletUpdate,BookletDelete,assignment_preview


app_name='assignment'

urlpatterns = [

    path('',home,name='home'),
    path('index',index,name='index'),
    path('index_jee_main',index_jee_main,name='index_jee_main'),
    path('index_jee_adv',index_jee_adv,name='index_jee_adv'),
    path('index_ssc',index_ssc,name='index_ssc'),
    path('index_others',index_others,name='index_others'),
    path('add_interest',add_interest,name='add_interest'),

    path('all-assignment',view_list_assignment,name='assignment_page'),
    path('myassignment',view_list_my_assignment,name='my_assignment_page'),
    path('myassignment/<pk>',view_list_my_assignment,name='my_assignment_page'),
    path('myassignment_update/<pk>',AssignmentUpdate.as_view(),name='my_assignment_update'),
    path('myassignment_delete/<pk>',AssignmentDelete.as_view(),name='my_assignment_delete'),
    path('assignment/add',assignmentCreate,name='assignment_add'),

    path('assignment/<slug>',assignment_preview,name='assignment_preview'),
    path('questionpaper/<slug>',QuestionView.as_view(),name='assignment'),
    path('assignment-like/<id>',AssignmentLikeToggle,name='like'),
    path('question/add/<pk>',QuestionAdd,name='question_add'),
    path('question/update/<pk>',QuestionUpdate.as_view(),name='question_update'),
    path('question/delete/<pk>',QuestionDelete.as_view(),name='question_delete'),
    path('assignment_check/<int:assignment_id>',assignment_check,name='assignment_check'),
    path('uploadfile/',booklet_upload,name='uploadfile'),

    path('search',SearchView.as_view(),name='search'),
    path('filter',filter_search,name='filter'),
    path('delete_interest/<pk>',InterestDelete.as_view(),name='delete_interest'),

    path('workbook_list',view_workbook_list,name='workbook_list'),
    path('workbook_list/<pk>',view_workbook_list,name='workbook_list'),

    path('workbook/<slug>',view_workbook,name='workbook'),

    path('create_workbook',add_workbook,name='add_workbook'),
    # path('my_blog_site_list',blog_site_list,name='blog_site'),
    # path('blog_site_list/<pk>',blog_site_list,name='blog_site'),

    path('page/<slug>',view_workbook_page,name='workbook_page'),
    path('add_page/<pk>',add_workbook_page,name='add_workbook_page'),

    path('result',result,name='result'),
    path('answersheet/<ass_id>-<ans_id>',answersheet,name='answersheet'),
    path('submissions/<pk>',show_submission,name='show_submission'),

    path('booklet',booklet,name='booklet'),
    path('booklet_preview/<slug>',booklet_preview,name='booklet_preview'),
    path('my-booklet',my_booklet,name='my-booklet'),
    path('my-booklet/<pk>',my_booklet,name='my-booklet'),
    path('index-booklet',index_booklet,name='index_booklet'),
    path('booklet/update/<pk>',BookletUpdate.as_view(),name='edit-booklet'),
    path('booklet/delete/<pk>',BookletDelete.as_view(),name='del-booklet'),


              ]