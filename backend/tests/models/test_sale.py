import unittest
from marketplace.models.sale import Sale


class SaleTestModel(unittest.TestCase):
    class_model = Sale
    field_id = 'id'
    app_label = 'marketplace'

    def setUp(self):
        super(SaleTestModel, self).setUp()

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
