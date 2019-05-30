from django.db import models


# Create your models here.

class Customer(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    age = models.IntegerField()
    profession = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.id} {self.firstname} {self.lastname}'
