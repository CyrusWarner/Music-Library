from django.db import models

# Create your models here.


class Song(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    album = models.CharField(max_length=50)
    release_date = models.DateField(blank=True)
    do_you_like_the_song = models.BooleanField(default=False, blank=True)
    likes = models.IntegerField(default=0)
    genre = models.CharField(max_length=50, default="", blank=True)
