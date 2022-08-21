from django.shortcuts import render
from django.http import HttpResponse

from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer

from rest_framework import viewsets

import datetime


def index(request):
    return HttpResponse('style_avenue_app/index.html')

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer