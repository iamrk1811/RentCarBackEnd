from rest_framework import serializers
from django.contrib.auth import authenticate
from account.models import User


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(required=True, min_length=6, max_length=128)

    def validate(self, data):
        email = data.get('email')
        password = data.get('password')
        if email and password:
            user = authenticate(email=email, password=password)
            if user:
                if not user.is_active:
                    msg = 'User account is disabled.'
                    raise serializers.ValidationError(msg)
                data['user'] = user
                return data
            else:
                msg = 'Incorrect Email/Password.'
                raise serializers.ValidationError(msg)
        else:
            msg = 'Must include "email" and "password"'
            raise serializers.ValidationError(msg)


class RegisterSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True, max_length=255)
    password = serializers.CharField(required=True, min_length=6, max_length=128)
    mobile = serializers.CharField(required=True, min_length=10, max_length=10)

    def validate_email(self, value):
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("Email id is already registered.")
        return value

    def validate_mobile(self, value):
        if User.objects.filter(mobile=value).exists():
            raise serializers.ValidationError("Mobile number is already registered.")
        return value
