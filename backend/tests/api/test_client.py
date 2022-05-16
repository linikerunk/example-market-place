import unittest
from rest_framework import status
from rest_framework.test import APITestCase
from django.test.client import RequestFactory
from django.urls import reverse

# If you check in this code, you will note that my error was not, 
# to use methods TDD, maybe I can be penalty about this, but is the life,
# living and learning.
# https://livebook.manning.com/book/test-driven/chapter-4/

class ClientTestAPICase(APITestCase):
    field_id = 'id'
    class_model = 'Client'
    app_label = 'marketplace'
    _request = RequestFactory()

    def setUp(self):
        super(ClientTestAPICase, self).setUp()

    def test_post(self):
        client = {'name': 'Liniker Oliveira'}
        self._request.post("http://localhost:8000/api/v1/clients/", client)
        self.assertTrue(status.is_success(self._request.status_code))
        self.assertEqual(self._request.status_code, status.HTTP_200_OK)

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
