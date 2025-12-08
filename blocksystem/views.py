from django.dispatch import receiver
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response

from instagram.serializers import Instaprofileserializers
from social.models import FollowRequest
from .models import Block
from .serializers import BlockSerializer
from instagram.models import Instaprofile
from rest_framework.permissions import IsAuthenticated

class BlockViewSet(viewsets.ModelViewSet):
    queryset = Block.objects.all()
    serializer_class = BlockSerializer 
    #permission_classes = [IsAuthenticated]  

    @action(detail=False, methods=['post'])
    def userblock(self, request):
        blocker = request.user.instaprofile  # logged-in user
        block_id = request.data.get('block_id')  # ID of user to block

        if not block_id:
            return Response({'detail': 'Please provide a block_id.'}, status=400)

        try:
            block_user = Instaprofile.objects.get(id=block_id)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'User does not exist.'}, status=404)

        if Block.objects.filter(block=block_user, blocker=blocker).exists():
            return Response({'detail': 'User is already blocked.'}, status=400)

        Block.objects.create(block=block_user, blocker=blocker)
        return Response({'detail': f'You have blocked {block_user.username}.'}, status=201)

    @action(detail=False, methods=['post'])
    def send_followrequest(self, request):
        sender = request.user.instaprofile
        receiver_id = request.data.get('receiver_id')

        if not receiver_id:
            return Response({'detail': 'Please provide receiver_id.'}, status=400)

        try:
            receiver = Instaprofile.objects.get(id=receiver_id)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'User does not exist.'}, status=404)

        # Check if blocked by receiver
        if Block.objects.filter(block=sender, blocker=receiver).exists():
            return Response({'detail': 'You are blocked by this user.'}, status=403)

        # Check if sender blocked the receiver
        if Block.objects.filter(block=receiver, blocker=sender).exists():
            return Response({'detail': 'You cannot send request to this user because you blocked them.'}, status=403)

        FollowRequest.objects.create(sender=sender, receiver=receiver, status='pending')
        return Response({'detail': f'Follow request sent to {receiver.username}.'}, status=201)

    @action(detail=False, methods=['get'])
    def view_profile(self, request, profile_id=None):
        viewer = request.user.instaprofile

        try:
            profile_user = Instaprofile.objects.get(id=profile_id)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'This user does not exist.'}, status=404)

        if Block.objects.filter(block=viewer, blocker=profile_user).exists():
            return Response({'detail': 'You are blocked by this user so you cannot view this profile.'}, status=403)

        serializer = Instaprofileserializers(profile_user)
        return Response(serializer.data)
