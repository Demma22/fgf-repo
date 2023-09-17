# serializers.py
from rest_framework import serializers
from .models import Contributor


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contributor
        fields = "__all__"
