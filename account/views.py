
from rest_framework import viewsets 
from django.contrib.auth.models import User
from .serializers import SignupSerializers
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView
from rest_framework.response import Response

class SignupViewSet(viewsets.ModelViewSet):
    serializer_class = SignupSerializers 
    queryset = User.objects.all()

class LogoutView(APIView):  # fixed class name
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response({"logout": "Logout successful"})
        except Exception as e:
            return Response({"detail": "The error is showing"})



# Create your views here.
