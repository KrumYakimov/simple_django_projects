import re

from django.core.exceptions import ValidationError


class FruitNameValidator:
    def __init__(self, message="Fruit name should contain only letters!"):
        self.message = message

    def __call__(self, value):
        if not re.match("^[A-Za-z]*$", value):
            raise ValidationError(self.message)

    def deconstruct(self):
        return (
            "fruitipedia.fruits.validators.FruitNameValidator",
            (),
            {"message": self.message},
        )
