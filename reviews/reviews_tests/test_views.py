from django.test import TestCase, Client
from django.urls import reverse


class TestViews(TestCase):

    def test_index_get(self):
        client = Client()
        response = client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
