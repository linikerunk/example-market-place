import unittest
from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse


class ClientTestAPICase(APITestCase):
    field_id = 'id'
    class_model = 'Client'
    app_label = 'marketplace'

    def setUp(self):
        super(ClientTestAPICase, self).setUp()

    def test_post(self):
        import ipdb; ipdb.set_trace();
        client = {'name': 'Liniker Oliveira'}
        response = self.client.post(
            "http://localhost:8000/api/v1/clients/",
            params=client
        )
        self.assertTrue(status.is_success(response.status_code))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get(self):
        url = reverse('clients')
        response = self.client.get(url)
        self.assertTrue(status.is_success(response.status_code))
    
    def test_put(self):
        ...

    def test_delete(self):

        ...


if __name__ == '__name__':
    unittest.main()
