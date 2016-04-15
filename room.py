import random
from setup import MONSTERS, ITEMS


class Room():
    def __init__(self, name=None):
        self.name = 'Some Random Room' if name is None else name
        self.items = random.sample(ITEMS, random.randint(0, 2))
        monster = random.sample(MONSTERS, random.randint(0, 1))
        self.monster = dict(monster[0]) if len(monster) > 0 else None

    def get_description(self):
        description = "\nThis is the %s." % self.name
        if len(self.items) > 0:
            description += "\nThere's some stuff on the floor."
            for index, item in enumerate(self.items):
                description += "\n%d. %s" % (index + 1, item['name'])
        if self.monster is not None:
            if self.monster['health'] > 0:
                description += "\nThere's a %s in here that looks angry." % self.monster['name']
            else:
                description += "\nThere's a dead %s laying on the floor." % self.monster['name']
        return description


    @staticmethod
    def _get_item(list_of_items):
        r = random.randint(0, len(list_of_items) - 1)
        return list_of_items[r]