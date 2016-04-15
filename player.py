from setup import ITEMS, STARTING_ITEM


class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.location = [0, 0]
        self.health = 100
        self.items = [ITEMS[STARTING_ITEM]]

    def get_description(self):
        description = "\n%s's health is %d and is carrying the following items " % (self.name, self.health)
        for index, item in enumerate(self.items):
            description += "\n%d. %s" % (index + 1, item['name'])
        return description
