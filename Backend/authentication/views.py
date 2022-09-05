import datetime
import jwt
from django.conf import settings
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status, views, viewsets
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .models import User
from .serializers import UserSerializer, RegisterSerializer, \
    EmailVerificationSerializer, LoginSerializer
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

        # absurl = 'http://' + "127.0.0.1:8080" + relative_link + "?token=" + str(token)

        email_body = 'Hi ' + user.username + \
                     ' Use the link below to verify your email \n' + absurl

        data = {
            'domain': current_site,
            # 'domain': "127.0.0.1:8080",
            'email_subject': 'Verify your email',
            'email_body': email_body,
            'to_email': user.email
        }
        Util.send_email(data)

        return Response(user_data, status=status.HTTP_201_CREATED)


class verifyEmail(views.APIView):
    serializer_class = EmailVerificationSerializer

    token_param_config = openapi.Parameter(
        'token', in_=openapi.IN_QUERY, description='Description', type=openapi.TYPE_STRING)

    @swagger_auto_schema(manual_parameters=[token_param_config])
    def get(self, request):
        id = request.GET.get('id')

        print(id)

        token = request.GET.get('token')
        print(token)
        try:
            email = request.GET.get('email')
            user = User.objects.filter(email=email).first()

            payload = {
                'id': user.id,
                'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
                'iat': datetime.datetime.utcnow()
            }

            token = jwt.decode(payload, settings.SECRET_KEY, algorithms=['HS256'])
            response = Response()

            # response.set_cookie(key='jwt', value=token, httponly=True)

            print('token decoded')
            if not user.is_verified:
                user.is_verified = True
                user.save()
            return Response({'email': 'Successfully activated'}, status=status.HTTP_200_OK)

        except jwt.ExpiredSignatureError as identifier:
            return Response({'error': 'Activation token is expired'}, status=status.HTTP_400_BAD_REQUEST)
        except jwt.exceptions.DecodeError as identifier:
            return Response({'error': 'Invalid token'}, status=status.HTTP_400_BAD_REQUEST)

        # response = Response()
        # print(serializer.data['access'])

        # response.set_cookie(key='jwt', value=serializer.data['access'], httponly=True)

        # payload = {
        #     'id': user.id,
        #     'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
        #     'iat': datetime.datetime.utcnow()
        # }
        #
        # token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')


class LoginAPIView(generics.GenericAPIView):
    serializer_class = LoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.get(email=request.data['email'])
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(request.data['password']):
            raise AuthenticationFailed('Incorrect password')

        return Response(serializer.data, status=status.HTTP_200_OK)


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, settings.SECRET_KEY, algorithm='HS256')

        response = Response()

        response.set_cookie(key='jwt', value=token, httponly=True)

        response.data = {
            'jwt': token
        }

        return response

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')

        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)

        return Response(serializer.data)

    def delete(self, request):
        response = Response()

        response.delete_cookie('jwt')

        response.data = {
            'message': 'success'
        }

        return response


class UserView(APIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated')
        try:
            payload = jwt.decode(token, settings.SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated')

        user = User.objects.filter(payload['id']).first()
        serializer = UserSerializer(user)

        return Response(token, serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }
        return response
