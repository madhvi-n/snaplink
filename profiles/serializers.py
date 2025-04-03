from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer, CharField, ValidationError


class UserSerializer(ModelSerializer):
    password = CharField(write_only=True, min_length=6, required=True)

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "is_active",
            "password",
        )
        read_only_fields = ("id", "is_active")

    def create(self, validated_data):
        """Create and return a new user with an encrypted password"""
        password = validated_data.pop("password", None)
        user = User(**validated_data)
        if password:
            user.set_password(password)
        user.save()
        return user


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        return {
            "access_token": data["access"],
            "refresh_token": data["refresh"],
        }
