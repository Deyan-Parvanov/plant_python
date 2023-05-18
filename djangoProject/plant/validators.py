from django.core import exceptions


def validate_capital_letter(value):
    if not value[0].isupper():
        raise exceptions.ValidationError("Your name must start with a capital letter!")


def validate_only_letters(value):
    if not value.isalpha():
        raise exceptions.ValidationError("Plant name should contain only letters!")
