class SchoolMap(object):
    pass


def start():
    player_name = input('What is your name? ')
    player = Player(player_name)
    map = SchoolMap()
    keep_going = True
    while keep_going:
        keep_going = do_command(player, map)


def do_command(player, map):
    sentence = input('Hi '+player.name+'. So, what do you want to do? ').lower()

    command = sentence.split(' ')[0]
    try:
        if command == 'help':
            display_help()
        elif command == 'quit':
            health(player)
            print('bye ', player.name)
            return False
        elif command == 'attack':
            item_name = sentence.split(' ')[2]
            attack(player, map, item_name)
        elif command == 'go':
            direction = sentence.split(' ')[1]
            go(player, map, direction)
        elif command == 'where':
            where_am_i(player, map)
        elif command == 'look':
            look_around(player, map)
        elif command == 'take':
            item_name = sentence.split(' ')[1]
            take(player, map, item_name)
        elif command == 'health':
            health(player)
        elif command == 'dude':
            dude()

    except Exception as e:
        print(player['name'] + '\'s brain sez, "I don\'t understand - ' + sentence + '"')
    return True


def dude():
    print("I know what dude I am!\nI'm the dude, playing a dude, disguised as another dude!")


def display_help():
    print("""
Your commands are\n
help\n
quit\n
attack with item\n
go direction\n
where am i\n
look around\n
take item\n
health\n""")


def attack(player, map, item_name):
    # check player for item
    did_attack = False
    for index, item in player.items:
        if item_name == item['name']:
            # attack
            # counter attack
            did_attack = True
            break
    # get player health
    # get monster
    # attack
    # check health and change name if negative

    pass


def go(player, map, direction):
    pass


def where_am_i(player, map):
    pass


def look_around(player, map):
    pass


def take(player, map, item_name):
    found = False
    for index, item in enumerate(map[player['location']].items):
        if item_name == item['name']:
            player.items.append(item)
            del map[player['location']].items[index]
            found = True
            break
    if found:
        print('The ' + item_name + ' is yours.')
    if not found:
        print('There is no ' + item_name + ' in ' + map[player['location']].name + '.')


def health(player):
    dude()
    print(player['name'], 'Health', player['health'], 'Items', player['items'])


FIRST_ITEM = 0
ITEMS = [
    {'name': 'spoon', 'attack': 2},
    {'name': 'sword', 'attack': 8},
    {'name': 'chair', 'attack': 5},
    {'name': 'thimble', 'attack': 1},
    {'name': 'branch', 'attack': 6},
    {'name': 'book', 'attack': 4},
    {'name': 'marker', 'attack': 2},
    {'name': 'teacher', 'attack': 4}
]


class Player():
    def __init__(self, player_name):
        self.name = player_name
        self.location = [0, 0]
        self.health = 100
        self.items = [ITEMS[FIRST_ITEM]]