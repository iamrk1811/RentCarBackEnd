from rest_framework import serializers

class LoginResponseSchema(serializers.Serializer):
    access = serializers.CharField(required=False)
    refresh = serializers.CharField(required=False)