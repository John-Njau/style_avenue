from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics,filters
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product
from .serializers import ProductSerializer


# Create your views here.
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductsCategoryView(APIView):
    def get(self, request, category):
        products = Product.objects.filter(category__name=category)
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)


class SearchProduct(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'category']

    def get(self, request, search):
        products = Product.objects.filter(name__icontains=search)

        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
