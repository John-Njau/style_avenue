from rest_framework import serializers

from .models import Product, Category, User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ('id',)


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, max_length=128, min_length=6, required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        read_only_fields = ('id',)

    def validated(self, attrs):
        email = attrs.get('email', '')
        username = attrs.get('username', '')

        if not username.isalnum():
            raise serializers.ValidationError('Username must be alphanumeric')
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
