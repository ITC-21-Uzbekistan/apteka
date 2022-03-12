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
    srok = models.DateField()
    date_dobavlen = models.DateField(auto_now_add=True)
    olingan_narxi = models.FloatField()
    ustiga_foiz = models.FloatField()
    sotiladigan_narx = models.FloatField()
    max_sena = models.FloatField()

    def __int__(self):
        return self.nakladnoy_no


class Pereotsenka(models.Model):
    tovar_id = models.BigIntegerField()
    eski_protsent = models.FloatField()
    eski_narx = models.FloatField()
    yengi_foiz = models.FloatField()
    yengi_narx = models.FloatField()
    changed_time = models.DateField(auto_now_add=True)

    def __int__(self):
        return self.tovar_id


class Spisaniya(models.Model):
    nakladnoy = models.BigIntegerField()
    tovar = models.BigIntegerField()
    olingan_soni = models.IntegerField()
    ishlab_chiqaruvchi = models.CharField(max_length=300)
    dori_sertifikati = models.CharField(max_length=200)
    srok = models.DateField()
    date_dobavlen = models.DateField(auto_now_add=True)
    olingan_narxi = models.FloatField()
    ustiga_foiz = models.FloatField()
    sotiladigan_narx = models.FloatField()
    when_spisano = models.DateField(auto_now_add=True)
    spisano = models.BooleanField()

    def __str__(self):
        return self.tovar