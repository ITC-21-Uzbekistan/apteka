from django.db import models
from kassir.models import Kassir


class Arxiv(models.Model):
    nakladnoy = models.BinaryField()
    tovar_name = models.CharField(max_length=500)
    tovar_shtrix_kod = models.BigIntegerField()
    tovar_shtuk_pachke = models.IntegerField()
    tovar_type = models.CharField(max_length=500)
    narx = models.FloatField()
    srok = models.DateField()
    soni = models.BigIntegerField()
    summa = models.FloatField()
    sold = models.DateTimeField()
    user = models.ForeignKey(Kassir, on_delete=models.CASCADE)

    def __str__(self):
        return self.tovar_name
