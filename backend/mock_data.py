from faker import Faker
from backend.marketplace.models.base import Sale
from backend.user.models.client import Client, Seller


fake = Faker()


for _ in range(10):
   Client.objects.create(name=fake.name())

for _ in range(10, 20):
   Seller.objects.create(name=fake.name())

for index in range(10):
    client_id = Client.object.get(id=index)
    seller_id = Seller.object.get(id=index)
    Sale.objects.create(
        client_id=client_id,
        seller_id=seller_id,
        operation_date=fake.date_time(),
    )
