from rest_framework import serializers
from .models import *

class AktyorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    ism = serializers.CharField(max_length=500)
    tugilgan_yil = serializers.DateField()
    jins = serializers.CharField(max_length=200)
    davlat = serializers.CharField(max_length=200, allow_blank=True)

    def validate_ism(self, qiymat):
        if len(qiymat) > 3:
            return qiymat
        raise serializers.ValidationError("Ism bunday kichik bo'lmaydi!")

class TarifSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    nom = serializers.CharField(max_length=500)
    narx = serializers.FloatField()
    muddat = serializers.CharField(max_length=500)

class KinoSerializer(serializers.ModelSerializer):
    aktyorlar = AktyorSerializer(many=True, read_only=True)
    class Meta:
        model = Kino
        fields = '__all__'

    def validate_nom(self, qiymat):
        if len(qiymat) > 3:
            return qiymat
        raise serializers.ValidationError("Nom bunday kichik bo'lmaydi!")

class KinoCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kino
        fields = '__all__'

class IzohSerializer(serializers.ModelSerializer):
    kino = KinoSerializer(many=True, read_only=True)
    class Meta:
        model = Kino
        fields = '__all__'

class IzohCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Izoh
        fields = '__all__'