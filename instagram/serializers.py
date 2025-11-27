from rest_framework import serializers 
#from.models import Instafollowers,Instaprofile 
from .models import Instafollowers, Instaprofile


class Instaprofileserializers(serializers.ModelSerializer):
    class Meta:
        model=Instaprofile
        fields='__all__'

class Instafollowersserializers(serializers.ModelSerializer):
    followeruser = Instaprofileserializers(read_only=True)
    followinguser = Instaprofileserializers(read_only=True)
    followeruser_id = serializers.PrimaryKeyRelatedField(
        queryset=Instaprofile.objects.all(), source='followeruser', write_only=True
    )
    followinguser_id = serializers.PrimaryKeyRelatedField(
        queryset=Instaprofile.objects.all(), source='followinguser', write_only=True
    )
    class Meta:
        model=Instafollowers
        fields='__all__'

