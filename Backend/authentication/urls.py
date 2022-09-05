from django.urls import path, include
from . import views

from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('email-verify/', views.verifyEmail.as_view(), name='email-verify'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
    path('user/', views.UserView.as_view(), name='user'),
    path('user-login/', views.LoginView.as_view(), name='user-login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
]
