from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='userpost')
    caption=models.TextField(null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='user')
    created_at=models.DateTimeField(auto_now_add=True)
    post=models.ForeignKey(Post,on_delete=models.CASCADE,related_name='comment')
    text=models.TextField(null=False,blank=False) # mendatory 
    parent=models.ForeignKey('self',on_delete=models.CASCADE,related_name='replies',null=True,blank=True)

class Likecomment(models.Model):
    comment=models.ForeignKey(Comment,on_delete=models.CASCADE,related_name='likepost')
    created_at=models.DateTimeField(auto_now_add=True)




# Create your models here.
