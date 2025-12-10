from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import NotificationSerializer  # singular
from .models import Notifications

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.received_notifications.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)





# Create your views here.
