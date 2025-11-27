from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import SignupViewSet,LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView




router=DefaultRouter()
router.register('signup',SignupViewSet,basename='signup')
urlpatterns=[
    path('',include(router.urls)),
    path('login/',TokenObtainPairView.as_view(),name='TokenObtainPairView'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), 
    path('logout/', LogoutView.as_view(), name='logout'),


]


