from faker import Faker
from random import random
from string import string
fake = Faker()


def _generate_full_record():  # -> dict

    ip = fake.ipv4()

    data = {
        'phone': fake.phone_number(),
        'credit_card': fake.credit_card_number(),
        'account_number': fake.ban(),
        'email': fake.email,
        'ip_address': fake.ipv4(),
        'mac_address': fake.mac_address(),
        'passport': fake.passport_number(),
        'driver_license': random.choices(string.digits, k=9) + ''.join(random.choices(string.digits, k=8)),
        'url': fake.url(),        'address': fake.address().replace("\n", ", "),
        "dob": fake.date_of_birth().strftime("%Y-%m-%d"),
        "license_plate": fake.license_plate(),
        "vin": fake.vin(),
        "tax_id": ''.join(random.choices(string.digits, k=9)),
        "bank_account": fake.iban(),
        "username": '',
        "password": '',
        "credit_score": random.randint(300, 850),
        "gender": random.choices(["male", "female", "other"]),
        "prefix": fake.prefix(),
        "suffix": fake.suffix(),
        "nickname": fake.first_name(),
        "latitude": fake.latitude(),
        "longitude": fake.longitude()
    }
    return data


def get_single_entity_records(count: int):
    records = [_generate_full_record() for _ in range(count)]

    return records
