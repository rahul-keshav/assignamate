from django.contrib import admin
from .models import UserAccount

# Register your models here.
class UserAccountAdmin(admin.ModelAdmin):
    list_display = ('user','userinfo','contact_no','city','website')

    def userinfo(self,object):
       return object.discription

    def get_queryset(self, request):
        queryset= super(UserAccountAdmin,self).get_queryset(request)
        queryset=queryset.order_by('-contact_no','user')
        return queryset


    userinfo.short_description = 'info'



admin.site.register(UserAccount,UserAccountAdmin)