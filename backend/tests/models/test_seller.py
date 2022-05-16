import unittest
from user.models.seller import Seller



class SellerTestModel(unittest.TestCase):
    class_model = Seller
    field_id = 'id'
    app_label = 'users'

    def setUp(self):
        super(SellerTestModel, self).setUp()

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
