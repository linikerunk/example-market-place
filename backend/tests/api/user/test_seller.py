import unittest
from django.urls import reverse
from marketplace.serializers.product_activity import ProductActivity
from user.serializers.seller import SellerSerializer



class SellerTestAPICase(unittest.TestCase):
    serializer_class = SellerSerializer
    field_id = 'id'
    class_model = 'SellerSerializer'
    app_label = 'users'

    def setUp(self):
        super(SellerTestAPICase, self).setUp()

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
