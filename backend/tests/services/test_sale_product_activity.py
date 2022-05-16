import unittest
from marketplace.services.sale_product_activity import SaleProductActivityService


class SaleProductActivityTestService(unittest.TestCase):
    class_services = SaleProductActivityService
    field_id = 'id'
    class_model = 'SaleProductActivity'
    app_label = 'marketplace'

    def setUp(self):
        super(SaleProductActivityService, self).setUp()

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
