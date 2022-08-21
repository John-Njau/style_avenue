from django.urls import path, include
from django.db import router

from rest_framework import routers

from  . import views

router=routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
router.register(r'categories', views.CategoryViewSet)

urlpatterns = [
    path('', views.index, name='index'),
    path('time',views.current_datetime),
    path('', include(router.urls)),
]