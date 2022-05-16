import unittest
from marketplace.models.product_activity import ProductActivity


class ProductActivityTestModel(unittest.TestCase):
    class_model = ProductActivity
    field_id = 'id'
    app_label = 'marketplace'

    def setUp(self):
        super(ProductActivityTestModel, self).setUp()

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
