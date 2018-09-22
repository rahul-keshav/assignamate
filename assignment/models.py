from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse
from django.utils.timezone import now
from django.db.models import Q
#############


class AssignmentQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(user__first_name__icontains=query) |
                         Q(title__icontains=query) |
                         Q(category__icontains=query) |
                         Q(discription__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs

    def intrests(self,intrest):
        qs = self
        if intrest is not None:
            or_lookup = (Q(user__first_name__icontains=intrest) |
                         Q(user__username__icontains=intrest) |
                         Q(title__icontains=intrest) |
                         Q(category__icontains=intrest)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs

    def jee_main(self):
        return self.filter(category='jee_main')

    def jee_adv(self):
        return self.filter(category='jee_advance')

    def ssc(self):
        return self.filter(category='ssc')

    def others(self):
        return self.filter(category='others')



class AssignmentManager(models.Manager):
    def get_queryset(self):
        return AssignmentQuerySet(self.model,using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

    def intrests(self,intrest):
        return self.get_queryset().intrests(intrest=intrest)

    def jee_main(self):
        return self.get_queryset().jee_main()
    def jee_adv(self):
        return self.get_queryset().jee_adv()
    def ssc(self):
        return self.get_queryset().ssc()
    def others(self):
        return self.get_queryset().others()


################
class BookletQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(user__first_name__icontains=query) |
                         Q(name__icontains=query) |
                         Q(discription__icontains=query)|
                         Q(subject__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs
class BookletManager(models.Manager):
    def get_queryset(self):
        return BookletQuerySet(self.model,using=self._db)

    def search(self,query=None):
        return self.get_queryset().search(query=query)

######################


class Assignment_answerd_byQuerySet(models.QuerySet):
    def show_submission(self,pk):
        return self.filter(assignment_id=pk)


class Assignment_answerd_byManager(models.Manager):
    def get_queryset(self):
        return Assignment_answerd_byQuerySet(self.model, using=self._db)

    def show_submission(self,pk):
        return self.get_queryset().show_submission(pk=pk)

#####################

# Create your models here.
class Assignment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title=models.CharField(max_length=30,default='assignment')
    discription=models.CharField(max_length=500)
    category=models.CharField(max_length=30,blank=True)
    created = models.DateTimeField(auto_now=True)
    objects = AssignmentManager()
    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assignment:assignment_page')

class Assignmentlikecounter(models.Model):
    assignment=models.OneToOneField(Assignment,on_delete=models.CASCADE)
    user=models.ManyToManyField(User,blank=True)
    number_of_like=models.IntegerField(default=0)
    def __str__(self):
        return self.assignment.title



class Questions(models.Model,):
    assignment= models.ForeignKey(Assignment,on_delete=models.CASCADE)
    question= models.CharField(max_length=500)
    image= models.ImageField(upload_to='question_image//%Y/%m/%d/',blank=True,)
    answer= models.CharField(max_length=500)
    option_a =models.CharField(max_length=200,default=0)
    option_b =models.CharField(max_length=200,default=0)
    option_c =models.CharField(max_length=200,default=0)
    option_d =models.CharField(max_length=200,default=0)
    number_of_right_answered =models.IntegerField(default=0)
    number_of_wrong_answered =models.IntegerField(default=0)
    positive_marks =models.IntegerField(default=0)
    negative_marks =models.IntegerField(default=0)
    hint =models.CharField(max_length=500,blank=True)
    tags=models.CharField(max_length=45,blank=True)


    def __str__(self):
        return self.question

    def get_absolute_url(self):
        return reverse('assignment:assignment_page')


class Assignment_answered_by(models.Model):
    name_of_assignment=models.CharField(max_length=30)
    name_of_teacher=models.CharField(max_length=150,blank=True)
    assigner_username=models.CharField(max_length=150,blank=True)
    assignment_id=models.IntegerField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    answer_string=models.CharField(max_length=400)
    marks=models.IntegerField()
    total_marks=models.IntegerField()
    submitted=models.DateTimeField(default=now)

    objects = Assignment_answerd_byManager()


    def __str__(self):
        return self.user.first_name+' '+self.user.last_name

class Intrests(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    intrest=models.CharField(max_length=30)

    def __str__(self):
        return self.intrest


class Booklet(models.Model):
    name=models.CharField(max_length=30)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    subject=models.CharField(max_length=20)
    discription=models.CharField(max_length=500)
    document=models.FileField(upload_to='documents//%Y/%m/%d/')
    uploaded_at=models.DateField(auto_now=True)

    objects = BookletManager()

    def __str__(self):
        return self.name

class Blogsite(models.Model):
    name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    quotes=models.CharField(max_length=100,blank=True)
    discription = models.CharField(max_length=500,blank=True)
    background_image=models.ImageField(upload_to='blogger_image/')
    submitted = models.DateTimeField(default=now)
    def __str__(self):
        return self.name

class Blog_page(models.Model):
    title=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    blog_site=models.ForeignKey(Blogsite,on_delete=models.CASCADE)
    text=models.TextField()
    image = models.ImageField(upload_to='blog_image/',blank=True)
    submitted = models.DateTimeField(default=now)
    def __str__(self):
        return self.title


