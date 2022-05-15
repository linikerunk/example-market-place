from datetime import datetime, timedelta
from rest_framework.exceptions import ValidationError


class SaleProductActivityService():

    def __init__(self, **kwargs):
        ...
        
    def handle_commission_range(self, *args, **kwargs):
        if not (self.commission > 0 and self.commission < 10):
            raise ValidationError({
                    "message_error": f"A Comissão deve ser entre 0% a 10%" 
            })

    def verify_commission_time(self, *args, **kwargs):
        # # 00:00:00 --> 1652572800 

        # current_time = datetime.now()
        # (datetime(2010,1,1) - datetime(1970,1,1)).total_seconds()
        ...
    
