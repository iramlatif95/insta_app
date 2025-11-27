# instafollow/views.py
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import FollowRequest
from .serializers import FollowRequestSerializer
from instagram.models import Instaprofile
from instagram.serializers import InstaprofileSerializer

class FollowRequestViewSet(viewsets.ModelViewSet):
    queryset = FollowRequest.objects.all()
    serializer_class = FollowRequestSerializer

    # 1️⃣ Send follow request
    @action(detail=False, methods=['post'])
    def send_request(self, request):
        sender_id = request.data.get('sender')
        receiver_id = request.data.get('receiver')

        # Validate sender and receiver
        try:
            sender = Instaprofile.objects.get(id=sender_id)
            receiver = Instaprofile.objects.get(id=receiver_id)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'User not found.'}, status=status.HTTP_404_NOT_FOUND)

        # Prevent sending request to self
        if sender == receiver:
            return Response({'detail': 'You cannot follow yourself.'}, status=status.HTTP_400_BAD_REQUEST)

        # Prevent duplicate requests
        if FollowRequest.objects.filter(sender=sender, receiver=receiver).exists():
            return Response({'detail': 'Follow request already sent.'}, status=status.HTTP_400_BAD_REQUEST)

        # Create follow request
        follow_request = FollowRequest.objects.create(sender=sender, receiver=receiver)
        serializer = self.get_serializer(follow_request)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    # 2️⃣ Pending follow requests for current user
    @action(detail=False, methods=['get'])
    def pending(self, request):
        try:
            profile = Instaprofile.objects.get(user=request.user)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        pending_requests = FollowRequest.objects.filter(receiver=profile, status='pending')
        serializer = self.get_serializer(pending_requests, many=True)
        return Response(serializer.data)

    # 3️⃣ Accept follow request
    @action(detail=True, methods=['post'])
    def accept(self, request, pk=None):
        follow_request = self.get_object()
        follow_request.status = 'accept'
        follow_request.save()
        return Response({'status': 'accepted'}, status=status.HTTP_200_OK)

    # 4️⃣ Reject follow request
    @action(detail=True, methods=['post'])
    def reject(self, request, pk=None):
        follow_request = self.get_object()
        follow_request.status = 'reject'
        follow_request.save()
        return Response({'status': 'rejected'}, status=status.HTTP_200_OK)

    # 5️⃣ Followers (people who follow current user)
    @action(detail=False, methods=['get'])
    def followers(self, request):
        try:
            profile = Instaprofile.objects.get(user=request.user)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        followers_requests = FollowRequest.objects.filter(receiver=profile, status='accept')
        followers = [f.sender for f in followers_requests]  # Get Instaprofile objects
        serializer = InstaprofileSerializer(followers, many=True)
        return Response(serializer.data)

    # 6️⃣ Following (people current user follows)
    @action(detail=False, methods=['get'])
    def following(self, request):
        try:
            profile = Instaprofile.objects.get(user=request.user)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'Profile not found.'}, status=status.HTTP_404_NOT_FOUND)

        following_requests = FollowRequest.objects.filter(sender=profile, status='accept')
        following = [f.receiver for f in following_requests]  # Get Instaprofile objects
        serializer = InstaprofileSerializer(following, many=True)
        return Response(serializer.data)
