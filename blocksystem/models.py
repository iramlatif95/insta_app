from django.db import models
from instagram.models import Instaprofile

class Block(models.Model):
    block=models.ForeignKey(Instaprofile,on_delete=models.CASCADE,related_name='whoblock')
    blocker=models.ForeignKey(Instaprofile,on_delete=models.CASCADE,related_name='blockuser')
    created_at=models.DateTimeField(auto_now_add=True)

# Create your models here.
