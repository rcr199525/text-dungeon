'''
Stores all rooms in the game. Every room has its own description and features.
Use rooms as building blocks for dungeon generation

Must-have room attributes:
NAME, USERDESC, DESC, NORTH, SOUTH, EAST, WEST, UP, DOWN, GROUND, SHOP, ENEMIES, SEEN

Optional room attributes:
SHOPINTRO (Greetings if room is shop)
'''

from dictionaries import *

def get_room_exits(room):
    '''
    returns room's exits as a dictionary of {DIRECTION : DESTINATION, ...}
    '''
    exits = {}
    for direction in DIRECTIONS:
        if room[direction]:
            exits[direction] = ROOMS[room[direction]][NAME]
        else:
            pass
    return exits

# USERDESC is written in the form "You ...", It explains the player's feelings and orientation from their POV (Max 2 lines)
# DESC usually starts with (The, This, There is), describing the room and its components (Min 2 lines)
# GROUND stores items on the room ground
# SHOP stores items for sale, if empty there is no shop
# ENEMIES stores enemy ids, if empty there is no combat
# SEEN tracks wether the room was seen or it is first time
ROOMS = {
    'lumbridge': {
        NAME: 'Lumbridge',
        USERDESC: 'You are in the middle of a square, you feel lost in the crowd of people.',
        DESC: 'The square is large with a fountain in the middle, narrow, paved roads lead out of the castle.',
        NORTH: None,
        SOUTH: None,
        EAST: 'al kharid',
        WEST: 'draynor village',
        UP: None,
        DOWN: 'swamp',
        GROUND: ['fountain', 'apple', 'bread', 'coin'],
        SHOP: [],
        ENEMIES: [],
        SEEN: False,
    },
    'swamp': {
        NAME: "Lumbridge Swamp",
        USERDESC: 'You are in a slimy swamp.',
        DESC: 'This swamp seems dangerous, there may be green ogres lurking about.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: 'lumbridge',
        DOWN: None,
        GROUND: ['coin', 'apple'],
        SHOP: [],
        ENEMIES: ['spider', 'spider'],
        SEEN: False,
    },
    'draynor manor': {
        NAME: "Draynor Manor",
        USERDESC: 'You are in a dark, gloomy mansion.',
        DESC: 'Everything is untouched, covered in dust.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: 'draynor village',
        GROUND: ['dagger'],
        SHOP: [],
        ENEMIES: ['werewolf', 'wolf'],
        SEEN: False,
    },
    'draynor village': {
        NAME: 'Draynor Village',
        USERDESC: 'You are in a small village.',
        DESC: 'The air smells of warm, tasty bread.',
        NORTH: None,
        SOUTH: None,
        WEST: None,
        EAST: 'lumbridge',
        UP: 'draynor manor',
        DOWN: None,
        GROUND: [],
        SHOP: ['bread', 'cake'],
        SHOPINTRO: 'The bakery has some freshly baked pastry for sale\n# Have a look:',
        ENEMIES: [],
        SEEN: False,
    },
    'al kharid': {
        NAME: 'Al Kharid',
        USERDESC: "You are in a desert town.",
        DESC: 'The sand is coarse and rough and irritating and it gets everywhere.',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: 'lumbridge',
        UP: 'mine',
        DOWN: None,
        GROUND: [],
        SHOP: ['beef'],
        SHOPINTRO: 'The butcher has some cuts ready to go\n# Have a look:',
        ENEMIES: [],
        SEEN: False,
    },
    'mine': {
        NAME: 'Al Kharid Mine',
        USERDESC: 'You come to a dusty mine with various metals.',
        DESC: 'The mine is dark and possibly full of terrors',
        NORTH: None,
        SOUTH: None,
        EAST: None,
        WEST: None,
        UP: None,
        DOWN: 'al kharid',
        GROUND: ['coin'],
        SHOP: [],
        ENEMIES: ['spider', 'spider'],
        SEEN: False,
    }
}