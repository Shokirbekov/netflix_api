from unittest import TestCase

from film.serializers import *


# class TestAktyorSerializer(TestCase):
#     def test_aktyor(self):
#         aktyor = {
#             "id": 1,
#             "ism": "An",
#             "tugilgan_yil": "1983-08-20",
#             "jins": "Erkak",
#             "davlat": "USA"
#         }
#         serializer = AktyorSerializer(data=aktyor)
#         assert serializer.is_valid() == False
#         assert serializer.errors['ism'][0] == "Ism bunaqa kalta bo'lmaydi brat"

class TestKinoSerializer(TestCase):
    def test_kino(self):
        kino = {
            "id": 1,
            "aktyorlar": [1],
            "nom": "The Amazing Spider Man",
            "yil": "2012-05-23",
            "janr": "Triller, Boyevik, Superhero"
        }
        serializer = KinoCreateSerializer(data=kino)
        assert serializer.is_valid() == True
        assert serializer.validated_data["nom"] == "The Amazing Spider Man"