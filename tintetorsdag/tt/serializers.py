from django.contrib.auth.models import Group
from tintetorsdag.tt.models import User
from tintetorsdag.tt.models import Tint
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["url", "username", "is_tinting"]


class TintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tint
        fields = ["created", "user"]


class SetTintSerializer(serializers.Serializer):
    is_tinting = serializers.BooleanField(required=True)
