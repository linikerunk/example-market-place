from faker import Faker
from marketplace.models.base import Sale


clients = [
'Chase Ferguson'
'Miguel White'
'Ashlee Kim'
'Sarah Taylor'
'Crystal Moore'
'John Warren'
'Willie Graves'
'Dr. Tammy Woodward MD'
'Dr. Veronica Davis'
'Kyle Howard'
]

sellers = [
'Cassandra Thompson'
'Stephanie Mitchell'
'Michelle Brown'
'Amanda Phillips'
'Jacqueline Christensen'
'Diane Scott'
'Linda Green'
'Darlene Hill'
'Sarah Tapia'
'Beth Sherman'
]

fake = Faker()


for _ in range(10):
   print(fake.name())
   Client.objects.create(name=fake.name())

for _ in range(10, 20):
   print(fake.name())
   Seller.objects.create(name=fake.name())

for index in range(10):
    client_id = Client.object.get(id=index)
    seller_id = Seller.object.get(id=index)
    Sale.objects.create(
        client_id=client_id,
        seller_id=seller_id,
        operation_date=fake.date_time(),
   )
