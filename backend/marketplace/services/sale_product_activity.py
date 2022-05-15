from datetime import datetime, time
from rest_framework.exceptions import ValidationError


class SaleProductActivityService():

    def __init__(self, **kwargs):
        self.operation_date = kwargs.get('operation_date')
        self.commission = kwargs.get('commission')
        
    def handle_commission_range(self, *args, **kwargs):
        if not (self.commission > 0 and self.commission < 10):
            raise ValidationError({
                    "message_error": f"A Comissão deve ser entre 0% a 10%" 
            })

    def verify_commission_time(self, *args, **kwargs):
        date_operation = datetime.now().strptime(
            self.operation_date,
            "%Y-%m-%dT%H:%M:%SZ"
        ).time()
        if time(0, 0) <= date_operation <= time(12, 0):
            if self.commission > 5:
                self.commission = 5
        elif time(12, 0, 1) < date_operation  < time(23, 59, 59):
            if self.commission < 4:
                self.commission = 4
