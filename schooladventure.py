"""Where everything begins.

The player is created and the map is imported.
The game loop starts and only ends if the player chooses to quit.

"""
from player import Player
from schoolmap import school_map


def start():
    """Where everything gets kicked off

    Create the player and start the command loop.
    Only end if do_command returns False
    """
    player_name = input('What is your name? ')
    player = Player(player_name)
    keep_going = True
    while keep_going:
        keep_going = do_command(player)


def do_command(player):
    """Get a command and do something.

    1. Get a command from the player.
    2. If the command is found, pull any other data need for the command from the sentence.
    3. Call the command function.

    If a command is not found 'else' then show an error.
    If the command sentence is incomplete an exception is thrown 'except' and an error is shown.
    """
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
    """dude
    You can add your own funny commands.
    Just create a function and call it from the do_command() if statement
    """
    print("I know what dude I am!\nI'm the dude, playing a dude, disguised as another dude!")


def display_help():
    """help
    Add commands to this or leave them off to make them secret.
    """
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
    """attack with item
    Make sure the player has the item.
    Make sure that a live monster is in the room.
    Deduct monster health by the attack value on the item.
    Counter attack by the monster does the same to the player.
    If the monster health < 1 then it is dead.
    If the player's health is < 1 then the player becomes a zombie.
    """
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
    """go direction
    Player can travel north, south, east or west.
    Player may not go off the map...abyss.
    """
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
    """where am i
    List the details of the current room.
    """
    print(school_map[player.location].get_description())


def look_direction(location, direction):
    """Not a command. Prints the description of the room in the direction related to the players current location."""
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
    """look around
    List the current room description and list the names of all the rooms around the player.
    """
    print(school_map[player.location[0]][player.location[1]].get_description())
    look_direction(player.location, 'north')
    look_direction(player.location, 'east')
    look_direction(player.location, 'south')
    look_direction(player.location, 'west')


def take(player, item_name):
    """take item
    Make sure the item is in the room. If it is add to the player items and remove it from the room.
    """
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
    """health
    Show the players name, health and items.
    """
    print(player.get_description())


if __name__ == '__main__':
    start()