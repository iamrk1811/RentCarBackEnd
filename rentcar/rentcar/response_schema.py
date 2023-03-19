from rest_framework import serializers


class DefaultBadRequestSchema(serializers.Serializer):
    errors = serializers.DictField(required=False)
