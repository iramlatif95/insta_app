
from rest_framework import viewsets 
from.serializers import Instaprofileserializers,Instafollowersserializers
from rest_framework import generics,mixins 
from .models import Instaprofile, Instafollowers
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view


class InstaprofileViewSet(viewsets.ModelViewSet):
    queryset=Instaprofile.objects.all()
    serializer_class=Instaprofileserializers

class InstafollwerViewSet(viewsets.ModelViewSet):
    queryset=Instafollowers.objects.all()
    serializer_class=Instafollowersserializers


    

   
    




# Create your views here.
