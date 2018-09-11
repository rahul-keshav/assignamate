from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Q

# Create your models here.

class UserAccountQuerySet(models.QuerySet):
    def search(self, query=None):
        qs = self
        if query is not None:
            or_lookup = (Q(city__icontains=query) |
                         Q(user__first_name__icontains=query) |
                         Q(user__username__icontains=query) |
                         Q(discription__icontains=query)|
                         Q(contact_no__icontains=query)
                         )
            qs = qs.filter(or_lookup).distinct()  # distinct() is often necessary with Q lookups
        return qs


class UserAccountManager(models.Manager):
    def get_queryset(self):
        return UserAccountQuerySet(self.model,using=self._db)
    def search(self,query=None):
        return self.get_queryset().search(query=query)


class UserAccount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    discription=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    website=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile_image',blank=True)
    follower=models.ManyToManyField(User,related_name='is_following',blank=True)
    facebook=models.CharField(max_length=50,blank=True)
    instagram = models.CharField(max_length=50, blank=True)
    twitter=models.CharField(max_length=50,blank=True)
    google_plus = models.CharField(max_length=50, blank=True)
    linkedin = models.CharField(max_length=50, blank=True)

    objects = UserAccountManager()

    def __str__(self):
        return self.user.username


def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserAccount.objects.create(user=kwargs['instance'])
post_save.connect(create_profile, sender=User)
