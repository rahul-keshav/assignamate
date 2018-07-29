from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.

class UserAccount(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    discription=models.CharField(max_length=50)
    contact_no=models.CharField(max_length=15)
    city=models.CharField(max_length=20)
    website=models.CharField(max_length=20)
    image=models.ImageField(upload_to='profile_image',blank=True)
    follower=models.ManyToManyField(User,related_name='is_following',blank=True)
    facebook=models.CharField(max_length=50,blank=True)
    instagram=models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserAccount.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)
