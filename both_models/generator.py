from faker import Faker
import random

fake = Faker()

# Supported entities from Presidio SpaCy
ENTITY_TYPES = [
    "PERSON", "EMAIL_ADDRESS", "PHONE_NUMBER", "DATE_TIME", "CREDIT_CARD",
    "IP_ADDRESS", "IBAN_CODE", "NRP", "LOCATION", "URL", "US_DRIVER_LICENSE",
    "US_SSN", "US_PASSPORT"
]

def generate_sentence():
    """
    Generate a realistic sentence with 1-2 entities embedded.
    Return sentence + entity details (with type, start, end).
    """
    sentence_templates = [
        "My name is {person} and I live in {city}. You can reach me at {email}.",
        "Please contact {person} on {phone} regarding the issue.",
        "{person} booked flight tickets on {date} and paid using card {credit_card}.",
        "The server with IP {ip} was accessed by {person}.",
        "Visit {url} for more information or email {email}.",
        "Driver license {dl} belongs to {person} who resides in {city}.",
        "Passport number {passport} is registered under {person}.",
        "{person}'s SSN is {ssn} and works in {city}.",
    ]

    template = random.choice(sentence_templates)

    replacements = {
        "person": fake.name(),
        "city": fake.city(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "date": fake.date(),
        "credit_card": fake.credit_card_number(),
        "ip": fake.ipv4(),
        "url": fake.url(),
        "dl": fake.license_plate(),
        "passport": fake.bothify(text="P########"),
        "ssn": fake.ssn()
    }

    text = template.format(**replacements)

    # Find entity positions
    entities = []
    for key, val in replacements.items():
        start = text.find(val)
        if start != -1:
            end = start + len(val)
            entity_type = {
                "person": "PERSON",
                "city": "LOCATION",
                "email": "EMAIL_ADDRESS",
                "phone": "PHONE_NUMBER",
                "date": "DATE_TIME",
                "credit_card": "CREDIT_CARD",
                "ip": "IP_ADDRESS",
                "url": "URL",
                "dl": "US_DRIVER_LICENSE",
                "passport": "US_PASSPORT",
                "ssn": "US_SSN"
            }.get(key, None)

            if entity_type:
                entities.append({
                    "entity_type": entity_type,
                    "start": start,
                    "end": end,
                    "text": val
                })

    return {"text": text, "entities": entities}

def generate_dataset(n=10):
    """Generate n synthetic records."""
    return [generate_sentence() for _ in range(n)]
