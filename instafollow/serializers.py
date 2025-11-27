from rest_framework import serializers 
from .models import FollowRequest 

class FollowRequestSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField()
    receiver = serializers.StringRelatedField()
    class Meta:
        model = FollowRequest
        fields = '__all__'
