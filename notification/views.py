#from requests import Response, post
from rest_framework.response import Response

from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from media.models import Post
from .serializers import NotificationSerializer 
from .models import Notifications
from django.contrib.auth.models import User
from rest_framework import status


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return self.request.user.received_notifications.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
    

    # this is for the like 
    @action(detail=False, methods=['post'])
    def like(self, request, pk=None):
        try:
    
            post = Post.objects.get(id=pk)

        
            Notifications.objects.create(
                sender=request.user,
                receiver=post.user,
                notification_type='like',
                post=post,
                text=f"{request.user.username} liked your post."
            )

            return Response({'like': True}, status=status.HTTP_201_CREATED)

        except Post.DoesNotExist:
            return Response({'error': 'Post not found'}, status=status.HTTP_404_NOT_FOUND)
    
    @action(detail=True,methods=['post'])
    def mention(self,request,pk=None):
        try:
        
            post=self.get_object
            mention_user_id=request.data.get('mention_id')
            mention_user=User.objects.get(id=mention_user_id)
            Notifications.objects.create(
            sender=request.user,
            receiver=mention_user,
            notification_type='mention',
            post=post,
            text=f"{request.user.username} mentioned you."
            )
            return Response({'mention': True})

        except User.DoesNotExist:
    
            return Response({'mention': False})
        
    
    @action(detail=True,methods=['post'])    
    def comment(self,request,pk=None):
        post = self.get_object()
        comment_text=request.data.get(comment_id)
        Notifications.objects.create(
            sender=request.user,
            receiver=post.user,
            notification_type='comment',
            post=post,
            comment=comment,
            text=f"{request.user.username} is comment"
        )
        return Response({'comment': True})
    
    @action(detail=True,methods=['post'])
    def follow(self,request,pk=None):
        follow_user=request.data.get('follow_user')
        follow_user_id=User.objects.get(id=follow_user_id)
        Notifications.objects.create(
            sender=request.user,
            receiver=follow_user_id.user,
            ntotifcation_type='follow',
            text=f"{request.user.username} is followuser"

        )
        return Response({'follow': True})







# Create your views here.
