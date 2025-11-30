
from rest_framework import viewsets
from .serializers import Instaprofileserializers, Instafollowersserializers
from .models import Instaprofile, Instafollowers
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import status
from django.db.models import Q
from .models import Instaprofile, Instafollowers
from instagram.models import Instaprofile 
from social.models import FollowRequest
from blocksystem.models import Block 
from rest_framework.permissions import IsAuthenticated





class InstaprofileViewSet(viewsets.ModelViewSet):
    queryset = Instaprofile.objects.all()
    serializer_class = Instaprofileserializers
    permission_classes = [IsAuthenticated]

    # View own profile
    @action(detail=False, methods=['get'])
    def my_profile(self, request):
        profile = Instaprofile.objects.get(user=request.user)
        serializer = self.get_serializer(profile)
        return Response(serializer.data)

    # View other user profile
    @action(detail=True, methods=['get'])
    def other_profile(self, request, pk=None):
        try:
            other_profile = Instaprofile.objects.get(pk=pk)
        except Instaprofile.DoesNotExist:
            return Response({'detail': 'The profile does not exist'})

        #  user is blocked
        if Block.objects.filter(blocker=request.user, blocked=other_profile.user).exists() or \
        Block.objects.filter(blocker=other_profile.user, blocked=request.user).exists():
            return Response({'detail': 'You cannot view this profile because you are blocked'})

        #  request is accepted
        follow_accepted = FollowRequest.objects.filter(
            (Q(sender=request.user, receiver=other_profile.user) |
            Q(sender=other_profile.user, receiver=request.user)),
            status='accepted'
        ).exists()

        if not follow_accepted:
            return Response({'detail': 'Follow request is not accepted'})

    
        serializer = self.get_serializer(other_profile)
        return Response(serializer.data)


class InstafollwerViewSet(viewsets.ModelViewSet):
    queryset = Instafollowers.objects.all()
    serializer_class = Instafollowersserializers
