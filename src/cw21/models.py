from django.db import models


# Create your models here.
class ContactInfo(models.Model):
    phone = models.CharField(max_length=50, null=True, default=None)
    address = models.CharField(max_length=50, null=True, default=None)

    def __str__(self):
        return f'{self.address}'


class Person(models.Model):
    firstname = models.CharField(max_length=255, default=None)
    lastname = models.CharField(max_length=255, default=None)
    age = models.IntegerField()
    profession = models.CharField(max_length=255, default=None)
    contact_info = models.OneToOneField(
        ContactInfo, null=True,
        related_name='person',
        on_delete=models.SET_NULL,
    )
    group = models.ForeignKey(
        'Group',
        null=True,
        on_delete=models.SET_NULL,
        related_name='persons',
    )

    hobbies = models.ManyToManyField('Hobbie', related_name='persons')

    def __str__(self):
        return f'{self.firstname} {self.lastname}'


class Group(models.Model):
    serial_number = models.CharField(max_length=4, default=None)
    size = models.PositiveSmallIntegerField()
    start_date = models.DateField(null=False)
    finish_date = models.DateField(null=False)

    def __str__(self):
        return f'{self.serial_number}|{self.start_date}'


class Hobbie(models.Model):
   name = models.CharField(max_length=255, default=None)

   def __str__(self):
       return f'{self.name}'