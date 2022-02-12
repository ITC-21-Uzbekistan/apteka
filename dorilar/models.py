from django.db import models


class Firma(models.Model):
    firma = models.CharField(max_length=200)

    def __str__(self):
        return self.firma


class TipTovara(models.Model):
    tip = models.CharField(max_length=100)

    def __str__(self):
        return self.tip


class Tovar(models.Model):
    shtrixKod = models.BigIntegerField()
    name = models.CharField(max_length=200)
    tip_tovara = models.ForeignKey(TipTovara, on_delete=models.CASCADE)
    shtukPachke = models.IntegerField()

    def __str__(self):
        return self.name


class NakladnoyNo(models.Model):
    nakladnoy_nom = models.BigIntegerField(unique=True)
    postavshik = models.ForeignKey(Firma, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{}".format(self.nakladnoy_nom)


class Nakladnoy(models.Model):
    nakladnoy = models.ForeignKey(NakladnoyNo, on_delete=models.CASCADE, null=True)
    tovar = models.ForeignKey(Tovar, on_delete=models.CASCADE)
    olingan_soni = models.IntegerField()
    ishlab_chiqaruvchi = models.CharField(max_length=300)
    dori_sertifikati = models.CharField(max_length=200)
    olingan_narxi = models.FloatField()
    ustiga_foiz = models.FloatField()
    sotiladigan_narx = models.FloatField()
    max_sena = models.FloatField()

    def __int__(self):  
        return self.nakladnoy_no



