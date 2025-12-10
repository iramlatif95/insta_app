from django.urls import path,include 
from rest_framework.routers import DefaultRouters
from.views import NotificationViewSet

router=DefaultRouters()
router.register('notification',NotificationViewSet,basename='notification')

urlpatterns = [
    path('', include(router.urls)),
]