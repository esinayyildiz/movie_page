from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)


class Movie(models.Model):
    film_adi = models.CharField(max_length=100)
    aciklama = models.TextField()
    gorsel = models.CharField(max_length=100)
    anasayfa = models.BooleanField(default=False)


