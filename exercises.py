from faker import Faker
from operator import itemgetter


class Exercises:
    @staticmethod
    def ex_1(sort: str) -> list:
        fake = Faker('ru_RU')
        people_list = [{
            "first_name": fake.first_name_male(),
            "last_name": fake.last_name_male(),
            "phone_number": fake.phone_number()
        } for _ in range(100)]
        if sort == 'sort_by_first_name':
            people_list.sort(key=itemgetter('first_name'))
        elif sort == 'sort_by_last_name':
            people_list.sort(key=itemgetter('last_name'))
        else:
            people_list.sort(key=itemgetter('phone_number'))
        return people_list

