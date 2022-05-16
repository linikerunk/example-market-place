import unittest
from django.urls import reverse
from marketplace.serializers.sale_product_activity import SaleProductActivity


class SaleProductActivityTestAPICase(unittest.TestCase):
    serializer_class = SaleProductActivity
    field_id = 'id'
    class_model = 'SaleProductActivity'
    app_label = 'marketplace'

    def setUp(self):
        super(SaleProductActivityTestAPICase, self).setUp()

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
