from rest_framework import serializers
from blocksystem.models import Block
from instagram.serializers import Instaprofileserializers 

class BlockSerializer(serializers.ModelSerializer):
  
    class Meta:
        model=Block 
        fields='__all__'

