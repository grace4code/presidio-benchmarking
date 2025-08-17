from faker import Faker
import random
from custom_faker import get_single_entity_records


class Gen:
    def __init__(self):
        self.fake = Faker()

    def singleEntity(self, entity, count):

        result = get_single_entity_records(entity, count)
        return result
