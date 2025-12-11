from django.db import models
#from rest_framework import timezone
from django.contrib.auth.models import User
from django.utils import timezone
from media.models import Post



class Notifications(models.Model):
    NOTIFICATION_TYPE=(
        ('like','like'),
        ('follow','follow'),
        ('mention','mention'),
        ('comment','comment'),
    )

    #user=models.ForeignKey('User',on_delete=models.CASCADE)
    sender=models.ForeignKey(User,on_delete=models.CASCADE,related_name='sender_user')
    receiver=models.ForeignKey(User,on_delete=models.CASCADE,related_name='receiver_user')
    notification_type=models.CharField(max_length=20,choices=NOTIFICATION_TYPE)
    text=models.CharField(max_length=100,blank=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,null=True, blank=True)
    created_at=models.DateTimeField(default=timezone.now)
    read_only=models.BooleanField(default=False)
    


# Create your models here.
