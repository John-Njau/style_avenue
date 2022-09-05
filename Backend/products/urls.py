from django.urls import path, include
from rest_framework import routers

from . import views
from .views import ProductsCategoryView

router = routers.DefaultRouter()
router.register(r'products', views.ProductViewSet)
# router.register(r'products/category', views.ProductsCategoryView)

urlpatterns = [
    path('', include(router.urls)),
    path('products/category/<str:category>', ProductsCategoryView.as_view(), name='products-category'),
    path('search/product/query=<str:search>', views.SearchProduct.as_view(), name='search-product'),

]
