from django.core.validators import MinLengthValidator
from django.db import models

from fruitipedia.fruits.validators import FruitNameValidator


class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )

    def __str__(self):
        return self.name


class Fruit(models.Model):
    name = models.CharField(
        max_length=30,
        validators=[
            MinLengthValidator(2),
            FruitNameValidator()
        ]
    )
    image = models.URLField()
    description = models.TextField()
    nutrition = models.TextField(
        null=True,
        blank=True
    )
    category = models.ForeignKey(
        to=Category,
        on_delete=models.CASCADE,
        related_name="fruits",
        null=True
    )

    def __str__(self):
        return self.name
