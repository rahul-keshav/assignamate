from django.contrib import admin
from .models import Assignment,Questions,Booklet,\
    Assignment_answered_by,Blogsite,Blog_page,Assignmentlikecounter
# Register your models here.
admin.site.register(Assignment)
admin.site.register(Questions)
admin.site.register(Assignment_answered_by)
admin.site.register(Booklet)
admin.site.register(Blog_page)
admin.site.register(Blogsite)
admin.site.register(Assignmentlikecounter)


