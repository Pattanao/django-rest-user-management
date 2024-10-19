from django.contrib.auth.models import User
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from apps.users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"
