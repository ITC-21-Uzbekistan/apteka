from django.db import models


class Kassir(models.Model):
    name = models.CharField(max_length=500)
    surname = models.CharField(max_length=500)
    passport_seria = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=1000)

    def __str__(self):
        return self.name
