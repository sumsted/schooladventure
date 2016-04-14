import random


class Room():
    NAME = "A room"
    DESCRIPTION = "This is a plain room, nothing special"
    ATTACK = {"weapon": "effectiveness"}

    def __init__(self):
        self.items = [""]
        self.monster = {"": 0}

    def get_description(self):
        description = self.DESCRIPTION
        if self.monster.values()[0] > 0:
            description += "\nThere is a " + self.monster.keys()[0] + " in this room and he's really mad."
        return description

    def attack(self, weapon):
        r = random.randint(0, 9)



    @staticmethod
    def _get_item(list_of_items):
        r = random.randint(0,len(list_of_items)-1)
        return list_of_items[r]