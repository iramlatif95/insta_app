
from rest_framework import filters

from django.shortcuts import render
from rest_framework import viewsets 
from django.contrib.auth.models import User  
#from django.db.models import Q 
from media.models import Post,Hashtag 
from .serializers import UserSearchSerializer, HashtagSerializer, PostSearchSerializer


class UserViewSet(viewsets.ModelViewSet):
    serializer_class=UserSearchSerializer
    queryset=User.objects.all()
    filter_backends=[filters.SearchFilter]  # build in filter in drf 
    search_fields=['username','firstname','lastname']

class HashtagViewSet(viewsets.ModelViewSet):
    serializer_class= HashtagSerializer
    queryset=Hashtag.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields=['name']
    
class PostViewSet(viewsets.ModelViewSet):
    serializer_class=PostSearchSerializer
    queryset=Post.objects.all()
    filter_backends=[filters.SearchFilter]
    search_fields=['caption','tag_name']


    

    



# Create your views here.
