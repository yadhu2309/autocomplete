from faker import Faker
from .models import Names
fake = Faker()

def feed_db(n):
    for i in range(0, n):
        Names.objects.create(
            name=fake.name()
            )
