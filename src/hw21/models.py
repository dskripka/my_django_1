from django.db import models

# Create your models here.

class MusicBand(models.Model):
    name = models.CharField(max_length=255, default=None)
    style = models.CharField(max_length=255, default=None)
    birth_year = models.PositiveSmallIntegerField()


class Album(models.Model):
    band = models.ForeignKey(MusicBand, on_delete=models.CASCADE, related_name='albums')
    name = models.CharField(max_length=255, default=None)
    release_year = models.PositiveSmallIntegerField()

class Track(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE, related_name='tracks')
    name = models.CharField(max_length=255, default=None)
    duration = models.TimeField()
