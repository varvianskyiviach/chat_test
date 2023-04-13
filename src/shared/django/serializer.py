from rest_framework import serializers


class ResponceSerializer(serializers.Serializer):
    result = serializers.DictField()


class ResponceMultiSerializer(serializers.Serializer):
    results = serializers.ListField()
