from player import Player
from schoolmap import school_map


def start():
    player_name = input('What is your name? ')
    player = Player(player_name)
    keep_going = True
    while keep_going:
        keep_going = do_command(player)


def do_command(player):
    sentence = input('\nHi ' + player.name + '. So, what do you want to do? ').lower()
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
            attack(player, item_name)
        elif command == 'go':
            direction = sentence.split(' ')[1]
            go(player, direction)
        elif command == 'where':
            where_am_i(player)
        elif command == 'look':
            look_around(player)
        elif command == 'take':
            item_name = sentence.split(' ')[1]
            take(player, item_name)
        elif command == 'health':
            health(player)
        elif command == 'dude':
            dude()
        else:
            print('\n' + player.name + '\'s brain sez, "I don\'t understand - ' + sentence + '"')
            display_help()

    except Exception as e:
        print('\n' + player.name + '\'s brain sez, "I don\'t understand - ' + sentence + '"')
        display_help()
    return True


def dude():
    print("I know what dude I am!\nI'm the dude, playing a dude, disguised as another dude!")


def display_help():
    print("""
Your commands are:
help
quit
attack with item
go direction
where am i
look around
take item
health""")


def attack(player, item_name):
    attack_status = "\nThere was no attack. Either you don\'t have a %s or there is no monster." % item_name

    for index, item in enumerate(player.items):
        if item_name == item['name'] and school_map[player.location[0]][player.location[1]].monster['health'] > 0:
            print("\n%s shall feel the wrath of your %s." % (
            school_map[player.location[0]][player.location[1]].monster['name'], item['name']))
            if item['attack'] < 5:
                print("\nYou know, %s is not a very effective weapon." % item['name'])
            school_map[player.location[0]][player.location[1]].monster['health'] -= item['attack']
            if school_map[player.location[0]][player.location[1]].monster['health'] > 0:
                print("\n%s's health is now %d." % (school_map[player.location[0]][player.location[1]].monster['name'],
                                                    school_map[player.location[0]][player.location[1]].monster[
                                                        'health']))
                print("\n%s counter attacks NOW!" % school_map[player.location[0]][player.location[1]].monster['name'])
                player.health -= school_map[player.location[0]][player.location[1]].monster['attack']
                print("\nYou lose %d health points. \nYour health is now %d." %
                      (school_map[player.location[0]][player.location[1]].monster['attack'], player.health))
                if player.health < 1:
                    player.name = 'Zombie ' + player.name
                    print("\n%s, you are now a zombie!" % player.name)
                if player.health <= 10:
                    print("\n%s, your health is quite low!" % player.name)
            else:
                print("\n%s is now dead. Long live %s!" %
                      (school_map[player.location[0]][player.location[1]].monster['name'], player.name))
            attack_status = "\nAttack complete."
            break

    print(attack_status)


def go(player, direction):
    current_location = player.location
    try:
        if direction == 'north':
            player.location[0] -= 1
        elif direction == 'south':
            player.location[0] += 1
        elif direction == 'east':
            player.location[1] += 1
        elif direction == 'west':
            player.location[1] -= 1
        else:
            print('\n%s is not a direction. Try north, south, east or west.' % direction)
        look_around(player)
    except:
        player.location = current_location
        print('\nI think you just tried to jump into the abyss.')


def where_am_i(player):
    print(school_map[player.location].get_description())


def look_direction(location, direction):
    try:
        x, y = location
        if direction == 'north':
            x -= 1
        elif direction == 'south':
            x += 1
        elif direction == 'east':
            y += 1
        elif direction == 'west':
            y -= 1
        print("To the %s is %s" % (direction, school_map[x][y].name))
    except:
        print("To the %s is the abyss." % direction)


def look_around(player):
    print(school_map[player.location[0]][player.location[1]].get_description())
    look_direction(player.location, 'north')
    look_direction(player.location, 'east')
    look_direction(player.location, 'south')
    look_direction(player.location, 'west')


def take(player, item_name):
    found = False
    for index, item in enumerate(school_map[player.location[0]][player.location[1]].items):
        if item_name == item['name']:
            player.items.append(item)
            del school_map[player.location[0]][player.location[1]].items[index]
            found = True
            break
    if found:
        print('\nThe ' + item_name + ' is yours.')
    if not found:
        print('\nThere is no ' + item_name + ' in ' + school_map[player.location[0]][player.location[1]].name + '.')


def health(player):
    print(player.get_description())


if __name__ == '__main__':
    start()