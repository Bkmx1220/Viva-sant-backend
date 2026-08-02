from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import UserManager

class User(AbstractUser):
    username = None

    email = models.EmailField(unique=True)

    phone = models.CharField(
        max_length=20,
        blank=True,
        null=True,
    )

    profile_image = models.ImageField(
        upload_to="profiles/",
        blank=True,
        null=True,
    )

    birth_date = models.DateField(
        blank=True,
        null=True,
    )

    GENDER_CHOICES = (
        ("M", "Masculin"),
        ("F", "Féminin"),
        ("O", "Autre"),
    )

    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        blank=True,
        null=True,
    )

    height = models.FloatField(
        blank=True,
        null=True,
    )

    weight = models.FloatField(
        blank=True,
        null=True,
    )

    health_goal = models.CharField(
        max_length=100,
        blank=True,
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", "last_name"]

    def __str__(self):
        return self.email