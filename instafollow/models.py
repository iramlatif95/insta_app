from django.db import models
from instagram.models import Instaprofile

class FollowRequest(models.Model):
    STATUS_CHOICES=[
        ('pending','pending'),
        ('accept','accept'),
        ('reject','reject'),
    ]
    sender=models.ForeignKey(Instaprofile,on_delete=models.CASCADE,related_name='send')
    receiver=models.ForeignKey(Instaprofile,on_delete=models.CASCADE,related_name='receive')
    created_at=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=8,choices=STATUS_CHOICES,default='pending')


# Create your models here.
