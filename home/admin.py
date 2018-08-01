from django.contrib import admin
from home.models import Post,Friends,Assignment_discussion,Assignment_discussion_reply

# Register your models here.
admin.site.register(Post)
admin.site.register(Friends)
admin.site.register(Assignment_discussion)
admin.site.register(Assignment_discussion_reply)