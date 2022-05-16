import unittest
from django.urls import reverse
from marketplace.serializers.product_activity import ProductActivity


class ProductActivityTestAPICase(unittest.TestCase):
    serializer_class = ProductActivity
    field_id = 'id'
    class_model = 'ProductActivity'
    app_label = 'marketplace'

    def setUp(self):
        super(ProductActivityTestAPICase, self).setUp()

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
