
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InstaprofileViewSet, InstafollwerViewSet

router = DefaultRouter()
router.register('profiles', InstaprofileViewSet, basename='profiles')
router.register('followers', InstafollwerViewSet, basename='followers')

urlpatterns = [
    path('', include(router.urls)),
]







