from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from rest_framework import serializers
from django.contrib.auth.models import *


def validate_davlat(qiymat):
    davlatlar = ["O'zbekiston", "AQSH", "Angliya", "Xitoy", "USA"]
    if qiymat not in davlatlar:
        raise ValidationError("Bu davlatdan aktyor qo'shish mumkin emas!")

def validate_jins(qiymat):
    if qiymat != "Erkak" or qiymat != "Ayol":
        return qiymat
    raise serializers.ValidationError("O'zgasayyoraliklar qabul qilinmaydi!")

def validate_ism(qiymat):
    if len(qiymat) > 3:
        return qiymat
    raise serializers.ValidationError("Ism bunday kichik bo'lmaydi!")


class Aktyor(models.Model):
    ism = models.CharField(max_length=500, validators=[validate_ism])
    tugilgan_yil = models.DateField()
    jins = models.CharField(max_length=200, validators=[validate_jins])
    davlat = models.CharField(max_length=200, validators=[validate_davlat])
    def __str__(self):
        return self.ism

class Kino(models.Model):
    nom = models.CharField(max_length=500)
    yil = models.DateField()
    janr = models.CharField(max_length=500)
    aktyorlar = models.ManyToManyField(Aktyor)
    def __str__(self):
        return self.nom

class Tarif(models.Model):
    nom = models.CharField(max_length=500)
    narx = models.FloatField(validators=[MinValueValidator(3)])
    muddat = models.CharField(max_length=500)
    def __str__(self):
        return self.nom

class Izoh(models.Model):
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    text = models.TextField()
    sana = models.DateTimeField(auto_now_add=True)