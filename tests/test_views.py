from unittest import TestCase
from rest_framework.test import APIClient

from film.views import *
from film.models import *

class TestAktyorAPI(TestCase):

    def setUp(self) -> None:
        self.client = APIClient()

    def test_aktyorlar(self):
        natija = self.client.get('/aktors/')
        assert natija.status_code == 200
        aktyorlar = natija.data
        assert len(aktyorlar) == Aktyor.objects.count()

    def test_aktyor_valid(self):
        natija = self.client.get('/aktor/1/')
        assert natija.status_code == 200
        assert natija.data['ism'] == Aktyor.objects.get(id=1).ism