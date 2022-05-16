import unittest
from django.urls import reverse
from marketplace.serializers.sale import SaleSerializer


class SaleTestAPICase(unittest.TestCase):
    serializer_class = SaleSerializer
    field_id = 'id'
    class_model = 'Sale'
    app_label = 'marketplace'

    def setUp(self):
        super(SaleTestAPICase, self).setUp()

    def test_post(self):
        url = ''

    def test_get(self):
        ...
    
    def test_put(self):
        ...

    def test_delete(self):
        ...

if __name__ == '__name__':
    unittest.main()
