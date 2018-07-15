from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from .models import NightlyStat

class ModelTestCase(TestCase):
    """Testing the Entry model"""

    def setUp(self):
        self.alcohol = "one filthy dirty IPA"
        self.nightlystat = NightlyStat(alcohol=self.alcohol)

    def test_model_can_create_a_NS(self):
        oldcount = NightlyStat.objects.count()
        self.nightlystat.save()
        newcount = NightlyStat.objects.count()
        self.assertNotEqual(oldcount, newcount)

class ViewTestCase(TestCase):
    """Testing the Entry views"""

    def setUp(self):
        self.client = APIClient()
        self.nightlystat_data = {'alcohol': 'one glass of Merlot'}
        self.respone = self.client.post(
            reverse('create'),
            self.nightlystat_data,
            format="json")

    def test_api_can_create_a_nightlystat(self):
        """test that the api has create ability"""

        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
