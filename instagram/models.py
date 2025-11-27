from django.db import models
from django.contrib.auth.models import User


class Instaprofile(models.Model):
    #id=models.IntegerField(primary_key=True)
    first_name=models.CharField(max_length=50,blank=True)
    last_name=models.CharField(max_length=50,blank=True)
    username=models.CharField(max_length=50)
    email=models.EmailField()
    image=models.ImageField(upload_to='instaprofile/',blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE,related_name='user_insta_profile')
    
    def __str__(self):
        return self.username


class Instafollowers(models.Model):
    
    followeruser=models.ForeignKey(Instaprofile, on_delete=models.CASCADE,related_name='userfollwer')
    followinguser=models.ForeignKey(Instaprofile, on_delete=models.CASCADE,related_name='userfollowing')
    created_at=models.DateTimeField(auto_now_add=True)
   








# Create your models here.
