from django.db import models

# Create your models here.



class Notes_for_school(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    discription = models.CharField(max_length=500)
    level=models.IntegerField()
    school=models.CharField(max_length=35)


class Notes_for_college(models.Model):
    name=models.CharField(max_length=20)
    subject=models.CharField(max_length=20)
    discription=models.CharField(max_length=500)
    level=models.CharField(max_length=20)
    college_name=models.CharField(max_length=35)
