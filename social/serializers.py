
from rest_framework import serializers 
from .models import FollowRequest 
from instagram.models import Instaprofile

class FollowRequestSerializer(serializers.ModelSerializer):
    

    followers = serializers.StringRelatedField(source='sender', read_only=True)
    following = serializers.StringRelatedField(source='receiver', read_only=True)
   


    class Meta:
        model = FollowRequest
        fields = '__all__'

