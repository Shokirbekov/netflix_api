from django.shortcuts import redirect
from django.views import View
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.permissions import *
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from django.contrib.auth.models import *

from .serializers import *
from .models import *


class HelloApiView(APIView):
    def get(self, reqeust):
        content = {
            "xabar": "Salom, World!",
        }
        return Response(content)

    def post(self, request):
        data = request.data
        content = {
            "xabar": "Ma'lumot qo'shildi",
            "ma'lumot": data
        }
        return Response(content)

class AktyorAPIView(APIView):
    def get(self, request):
        aktyorlar = Aktyor.objects.all()
        serializer = AktyorSerializer(aktyorlar, many=True)
        return Response(serializer.data)

    def post(self, request):
        aktyor = request.data
        serializer = AktyorSerializer(data=aktyor)
        if serializer.is_valid():
            Aktyor.objects.create(
                ism = serializer.validated_data.get('ism'),
                tugilgan_yil = serializer.validated_data.get('tugilgan_yil'),
                jins = serializer.validated_data.get('jins'),
                davlat = serializer.validated_data.get('davlat'),
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class AktyorDetailView(APIView):
    def get(self, request, pk):
        aktyorlar = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyorlar)
        return Response(serializer.data)

    def put(self, request, pk):
        aktyor = Aktyor.objects.get(id=pk)
        serializer = AktyorSerializer(aktyor, data=request.data)
        if serializer.is_valid():
            aktyor.ism = serializer.validated_data.get('ism')
            aktyor.davlat = serializer.validated_data.get('davlat')
            aktyor.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TarifAPIView(APIView):
    def get(self, request):
        tariflar = Tarif.objects.all()
        serializer = TarifSerializer(tariflar, many=True)
        return Response(serializer.data)

# class KinoAPIView(APIView):
#     def get(self, request):
#         kinolar = Kino.objects.all()
#         serializer = KinoSerializer(kinolar, many=True)
#         return Response(serializer.data)
#
#     def post(self, request):
#         kino = request.data
#         serializer = KinoCreateSerializer(data=kino)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# class KinoDetailAPIView(APIView):
#     def get(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoSerializer(kino)
#         return Response(serializer.data)
#
#     def put(self, request, pk):
#         kino = Kino.objects.get(id=pk)
#         serializer = KinoSerializer(kino, data=request.data)
#         if serializer.is_valid():
#             serializer.nom = serializer.validated_data.get('nom')
#             serializer.janr = serializer.validated_data.get('janr')
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class KinoViewSet(ModelViewSet):
    queryset = Kino.objects.all()
    serializer_class = KinoSerializer

    @action(detail=True)
    def aktyorlar(self, request, pk):
        kino = Kino.objects.get(id=pk).aktyorlar.all()
        serializer = AktyorSerializer(kino, many=True)
        return Response(serializer.data)

class IzohAPIView(APIView):
    def get(self, request):
        izoh = Izoh.objects.all()
        serializer = IzohSerializer(izoh)
        return Response(serializer.data)
    def post(self, request):
         izoh = request.data
         serializer = IzohCreateSerializer(data=izoh)
         if serializer.is_valid():
             serializer.save()
             return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class IzohDeleteView(View):
    def get(self, request, pk):
        to_be_deleted = Izoh.objects.get(id=pk)
        if to_be_deleted and to_be_deleted.user == request.user:
            to_be_deleted.delete()
            return redirect('/izohlar/')
        return redirect('/izohlar/')