from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=250)
    body = serializers.CharField(max_length=1000000)
    publish = serializers.DateTimeField()
    created = serializers.DateTimeField()
    status = serializers.CharField(max_length=20)