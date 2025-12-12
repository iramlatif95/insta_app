from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, HashtagViewSet, PostViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'hashtags', HashtagViewSet)
router.register(r'posts', PostViewSet)

urlpatterns = [
    path('', include(router.urls)),
]

