from rest_framework.exceptions import ValidationError
from marketplace.models.product_activity import ProductActivity


class ProductActivityService():
    
    def __init__(self, **kwargs):
        self.name = kwargs.get('products')
        self.is_product = kwargs.get('is_product')
        self.price = kwargs.get('price')
        self.commission = kwargs.get('commission')

    def handle_commission_range(self, *args, **kwargs):
        if not (self.commission > 0 and self.commission < 10):
            raise ValidationError({
                    "message_error": f"A Comissão deve ser entre 0% a 10%" 
            })