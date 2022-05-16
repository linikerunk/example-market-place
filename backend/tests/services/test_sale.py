import unittest
from marketplace.services.product_activity import ProductActivityService


class ProductActivityTestService(unittest.TestCase):
    class_services = ProductActivityService
    field_id = 'id'
    class_model = 'ProductActivity'
    app_label = 'marketplace'

    def setUp(self):
        super(ProductActivityTestService, self).setUp()

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
