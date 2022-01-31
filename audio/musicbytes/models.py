from django.db import models


# Create your models here.
class Album(models.Model):
    name = models.CharField(max_length=250)
    composer = models.CharField(max_length=250)
    artist = models.CharField(max_length=250)
    year = models.IntegerField()
    img = models.ImageField(upload_to='gallery')
    lyric = models.CharField(max_length=250)

    def __str__(self):
        return self.name
