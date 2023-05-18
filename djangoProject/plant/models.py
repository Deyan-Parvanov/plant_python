from django.core import validators
from django.db import models

from djangoProject.plant.validators import validate_capital_letter, validate_only_letters


class ProfileModel(models.Model):
    USERNAME_MAX_LEN = 10
    USERNAME_NAME_MIN_LEN = 2
    NAME_MAX_LEN = 20
    LAST_NAME_MAX_LEN = 20

    username = models.CharField(
        max_length=USERNAME_MAX_LEN,
        validators=(
            validators.MinLengthValidator(USERNAME_NAME_MIN_LEN),
        ),
        blank=False,
        null=False,
    )

    first_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validate_capital_letter,
        ),
        blank=False,
        null=False,
    )

    last_name = models.CharField(
        max_length=NAME_MAX_LEN,
        validators=(
            validate_capital_letter,
        ),
        blank=False,
        null=False,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class PlantModel(models.Model):
    PLANT_MAX_CHARS = 14
    PLANT_NAME_MAX = 20
    PLANT_NAME_MIN = 2

    OUTDOOR_PLANTS = 'Outdoor Plants'
    INDOOR_PLANTS = "Indoor Plants"

    PLANTS = (
        (OUTDOOR_PLANTS, OUTDOOR_PLANTS),
        (INDOOR_PLANTS, INDOOR_PLANTS),
    )

    plant_type = models.CharField(
        max_length=PLANT_MAX_CHARS,
        choices=PLANTS,
        blank=False,
        null=False,
    )

    name = models.CharField(
        max_length=PLANT_NAME_MAX,
        validators=(
            validators.MinLengthValidator(PLANT_NAME_MIN),
            validate_only_letters,
        ),
        blank=False,
        null=False,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    description = models.TextField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
    )

    class Meta:
        ordering = ('pk',)

