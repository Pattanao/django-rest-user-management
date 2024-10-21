from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django_countries.serializers import CountryFieldMixin
from rest_framework import serializers

from apps.users.models import Profile


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name", "email"]


class ProfileSerializer(CountryFieldMixin, serializers.ModelSerializer):
    user = UserSerializer(read_only=False)
    age = serializers.IntegerField(
        validators=[
            MinValueValidator(18, message="Age must greater than 18."),
            MaxValueValidator(85, message="Age must less than 85."),
        ]
    )
    phone_number = serializers.CharField(
        validators=[
            RegexValidator(
                regex=r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$",
                message="Phone Number must be in valid format.",
            )
        ],
    )

    class Meta:
        model = Profile
        fields = "__all__"
