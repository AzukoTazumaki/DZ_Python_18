from faker import Faker
from operator import itemgetter
fake = Faker('ru_RU')

people_list = [{
    "first_name": fake.first_name_male(),
    "last_name": fake.last_name_male(),
    "phone_number": fake.phone_number()
} for _ in range(100)]

people_list.sort(key=itemgetter('first_name'))

print(people_list)