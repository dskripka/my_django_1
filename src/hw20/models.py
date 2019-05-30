from django.db import models
from django.core.validators import MinValueValidator

class Car(models.Model):
    brand = models.CharField(max_length=30, default=None)
    model = models.CharField(max_length=20, default=None)
    color = models.CharField(max_length=20, default=None)
    weight = models.PositiveSmallIntegerField(null=False)
    owner_full_name = models.CharField(max_length=50, default=None)
    year_issue = models.PositiveSmallIntegerField(null=False, validators=[MinValueValidator(1900)])

    def __str__(self):
        return f'{self.brand} {self.model}'
