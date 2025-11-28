from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FollowRequest
from .serializers import FollowRequestSerializer
from instagram.models import Instaprofile

class FollowRequestViewSet(viewsets.ModelViewSet):
    queryset = FollowRequest.objects.all()
    serializer_class = FollowRequestSerializer

    @action(detail=False, methods=['post'])
    def send_request(self, request):
        sender_id = request.data.get('sender')
        receiver_id = request.data.get('receiver')

        try:
            sender = Instaprofile.objects.get(id=sender_id)
            receiver = Instaprofile.objects.get(id=receiver_id)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        if sender == receiver:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        if FollowRequest.objects.filter(sender=sender, receiver=receiver).exists():
            return Response({'detail': 'Follow request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        follow_request = FollowRequest.objects.create(sender=sender, receiver=receiver)
        serializer = self.get_serializer(follow_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['get'])
    def pending(self, request):
        profile = Instaprofile.objects.get(user=request.user)
        pending_requests = FollowRequest.objects.filter(receiver=profile, status='pending')
        serializer = self.get_serializer(pending_requests, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        follow_request = self.get_object()
        follow_request.status = 'accept'
        follow_request.save()
        return Response({'status': 'accepted'})

    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        follow_request = self.get_object()
        follow_request.status = 'reject'
        follow_request.save()
        return Response({'status': 'rejected'})

    @action(detail=False, methods=['get'])
    def followers(self, request):
        profile = Instaprofile.objects.get(user=request.user)
        followers = FollowRequest.objects.filter(receiver=profile, status='accept')
        serializer = self.get_serializer(followers, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def following(self, request):
        profile = Instaprofile.objects.get(user=request.user)
        following = FollowRequest.objects.filter(sender=profile, status='accept')
        serializer = self.get_serializer(following, many=True)
        return Response(serializer.data)
    
    # this for thee unfolloww

    @action(detail=False, methods=['post'])
    def unfollow(self,request):
        sender_id=request.data.get('sender')
        receiver_id=request.data.get('receiver')

        try:
            sender=Instaprofile.objects.get(id=sender_id)
            receiver=Instaprofile.objects.get(id=receiver_id)
        except Instaprofile.DoesNotExist:
            return Response({'detail':'user not exists'})
        

        
        try:
            followrequest=FollowRequest.objects.get(sender=sender,receiver=receiver,status='accept')
    
        except FollowRequest.DoesNotExist:
            return Response({'detail': 'the follow request is not found'})
        
        followrequest.delete()
        return Response({'detail':'u unfollow or delete this request'})
        
    
    
    
    

    




# Create your views here.
