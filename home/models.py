from django.db import models
from django.contrib.auth.models import User
from assignment.models import Assignment
# Create your models here.
class Post(models.Model):
    post=models.TextField()
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)

class Friends(models.Model):
    user=models.ManyToManyField(User)

class Assignment_discussion(models.Model):
    assignment=models.ForeignKey(Assignment,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField(auto_now=True)
    comment=models.TextField()

class Assignment_discussion_reply(models.Model):
    assignment_discussion=models.ForeignKey(Assignment_discussion,on_delete=models.CASCADE)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    reply=models.TextField()
    date=models.DateTimeField(auto_now=True)