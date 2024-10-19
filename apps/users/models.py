from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator, RegexValidator
from django.db import models
from django_countries.fields import CountryField


class Profile(models.Model):
    MALE = "M"
    FEMALE = "F"
    GENDER_CHOICES = {MALE: "Male", FEMALE: "Female"}

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField(
        null=False, validators=[MinValueValidator(18), MaxValueValidator(85)]
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    address = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=30, blank=True)
    country = CountryField(blank=True)
    phone_number = models.CharField(
        max_length=20,
        blank=True,
        validators=[
            RegexValidator(
                regex=r"^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$",
            )
        ],
    )
