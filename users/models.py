from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    MALE_GENDER = "M"
    FEMALE_GENDER = "F"
    GENDER = [
        (MALE_GENDER, "Male"),
        (FEMALE_GENDER, "Female"),
    ]

    LANGUAGE_ENGLISH = "en"
    LANGUAGE_VIETNAMESE = "vn"
    LANGUAGE = [(LANGUAGE_ENGLISH, "English"), (LANGUAGE_VIETNAMESE, "Vietnamese")]

    CURRENCY_USD = "USD"
    CURRENCY_VND = "VND"
    CURRENCY = [(CURRENCY_USD, "USD"), (CURRENCY_VND, "VND")]

    EMAIL_LOGIN = "email"
    GITHUB_LOGIN = "github"

    LOGIN_METHOD = [(EMAIL_LOGIN, "Email"), (GITHUB_LOGIN, "Github")]

    avatar = models.ImageField(null=True)
    gender = models.CharField(max_length=255, choices=GENDER)
    bio = models.TextField(default="")
    birthdate = models.DateField(null=True)
    language = models.CharField(
        max_length=255, choices=LANGUAGE, default=LANGUAGE_ENGLISH
    )
    currency = models.CharField(max_length=255, choices=CURRENCY, default=CURRENCY_VND)
    superhost = models.BooleanField(default=False)
    login_method = models.CharField(max_length=10, choices=LOGIN_METHOD, default=EMAIL_LOGIN)
