from faker import Faker
import random

fake = Faker()

# Map Presidio entities to Faker methods
ENTITY_GENERATORS = {
    "EMAIL_ADDRESS": lambda: fake.email(),
    "PHONE_NUMBER": lambda: fake.phone_number(),
    "PERSON": lambda: fake.name(),
    "LOCATION": lambda: fake.city(),
    "DATE_TIME": lambda: fake.date_time().isoformat(),
    # National Registration?
    "NRP": lambda: str(fake.random_number(digits=6)),
    "IP_ADDRESS": lambda: fake.ipv4(),
    "CREDIT_CARD": lambda: fake.credit_card_number(),
    "IBAN_CODE": lambda: fake.iban(),
    "US_SSN": lambda: fake.ssn(),
    "US_DRIVER_LICENSE": lambda: fake.bothify(text="??######"),  # fake DL
    "US_PASSPORT": lambda: fake.bothify(text="A########"),
    "US_BANK_NUMBER": lambda: str(fake.random_number(digits=10)),
    "US_ITIN": lambda: fake.bothify("9##-##-####"),
    "ORGANIZATION": lambda: fake.company(),
    "URL": lambda: fake.url(),
    "USERNAME": lambda: fake.user_name(),
    "PASSWORD": lambda: fake.password(),
    "AGE": lambda: str(random.randint(18, 90)),
    "ZIP": lambda: fake.postcode()
}


def generate_fake_records(num_records=20):
    """Generate fake data for each Presidio entity type"""
    records = []
    for entity, generator in ENTITY_GENERATORS.items():
        for _ in range(num_records):
            records.append({"entity_type": entity, "text": generator()})
    return records
