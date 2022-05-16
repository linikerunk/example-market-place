import unittest


class ClientTestAPICase(unittest.TestCase):
    field_id = 'id'
    class_model = 'Client'
    app_label = 'marketplace'

    def setUp(self):
        super(ClientTestAPICase, self).setUp()

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
