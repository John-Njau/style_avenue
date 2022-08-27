from django.urls import path, include
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)
# router.register(r'orders', views.OrderViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('time/', views.current_datetime),
    path('index/', views.index, name='index'),
    path('email-verify/', views.verifyEmail.as_view(), name='email-verify'),
    path('register/', views.RegisterView.as_view(), name='register'),
    path('login/', views.LoginAPIView.as_view(), name='login'),
]
