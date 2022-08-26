import datetime

from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponse
from django.urls import reverse

from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

from .models import Product, Category, User
from .serializers import ProductSerializer, CategorySerializer, UserSerializer, RegisterSerializer
from .utils import Util


class RegisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_data = serializer.data

        user = User.objects.get(email=user_data['email'])

        token = RefreshToken.for_user(user).access_token

        current_site = get_current_site(request).domain

        relative_link = reverse('email-verify')

        absurl = 'http://' + current_site + relative_link + "?token=" + str(token)

        email_body = 'Hi ' + user.username + \
                     ' Use the link below to verify your email \n' + absurl

        data = {
            'domain': current_site,
            'email_subject': 'Verify your email',
            'email_body': email_body,
            'to_email': user.email
        }
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class verifyEmail(generics.GenericAPIView):
    def get(self):
        pass


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


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
