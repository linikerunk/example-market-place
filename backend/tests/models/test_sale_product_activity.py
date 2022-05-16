import unittest
from marketplace.models.sale_product_activity import SaleProductActivity


class SaleProductActivityModel(unittest.TestCase):
    class_model = SaleProductActivity
    field_id = 'id'
    app_label = 'marketplace'

    def setUp(self):
        super(SaleProductActivityModel, self).setUp()

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
