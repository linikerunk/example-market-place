import unittest
from user.models.client import Client


class ClientTestModel(unittest.TestCase):
    class_model = Client
    field_id = 'id'
    app_label = 'marketplace'

    def setUp(self):
        super(ClientTestModel, self).setUp()

    def test_post(self):
        ...

    def test_get(self):
        ...
    
    def test_put(self):
        ...

    def test_delete(self):
        ...


if __name__ == '__name__':
    unittest.main()
