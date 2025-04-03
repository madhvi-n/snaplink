from .models import URL
from rest_framework import serializers


class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ("original_url", "new_url", "one_time_use", "expires_at")
        read_only_fields = (
            "id",
            "uuid",
            "new_url",
            "created_at",
            "updated_at",
            "clicks",
        )


class URLReadOnlySerializer(serializers.Serializer):
    original_url = serializers.CharField(read_only=True)
    new_url = serializers.CharField(read_only=True)
    expires_at = serializers.DateTimeField(read_only=True)
    one_time_use = serializers.BooleanField(read_only=True)
