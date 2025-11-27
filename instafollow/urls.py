from django.urls import path,include 
from rest_framework.routers import DefaultRouter 
from.views import FollowRequestViewSet 

router=DefaultRouter()
router.register('followrequest',FollowRequestViewSet, basename='followrequest'),
urlpatterns=[
    path('', include(router.urls)),
]