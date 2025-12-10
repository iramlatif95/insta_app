from rest_framework import serializers
from notification.models import Notifications


class NotificationSerializers(serializers.ModelSerializer):
    
    class Meta:
        model=Notifications 
        fields='__all__'

