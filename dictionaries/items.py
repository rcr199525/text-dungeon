'''
Stores all items in the game. An item is anything you can pick,
store in inventory, look at, or eat.

Must-have item attributes:
NAME, GROUNDDESC, SHORTDESC, LONGDESC, PICKABLE, EDIBLE, TAG

Optional item attributes:
PRICE (If sold in a shop), WEAPON (If used as weapon)
'''

from dictionaries import *
from dictionaries.weapon_skills import WEAPONS, SKILLS

# returns list of the names of items with a specified tag assigned to them
def get_tag_items(item_names, tag):
    tag_items = []
    for name in item_names:
        if ITEMS[name][TAG] == tag:
            tag_items.append(name)
    return tag_items

# returns items GROUNDDESC as bullet point
def get_items_grounddesc(room, item_look = None):
    text = ''
    for item_name in room[GROUND]:
        item = ITEMS[item_name]
        # add item GROUNDDESC to be displayed
        if type(item[GROUNDDESC]) is list:
            text += '{} {} {}'.format(BULLET + item[GROUNDDESC][0],
            item[NAME].lower(), item[GROUNDDESC][1] + '\n')
        elif type(item[GROUNDDESC]) is str:
            text += BULLET + item[GROUNDDESC] + '\n'

    return text

def get_items_shortdesc(item_names):
    text = ''
    for item_name in item_names:
        item = ITEMS[item_name]
        # add item SHORTDESC to be displayed
        text += BULLET + item[SHORTDESC] + '\n'
    return text

# coin items and their values                     
COIN_VALUE = {
    'coin': 1,
    'gold coin': 7,
    'coins sack': 10,
    'gold coins sack': 70,
}

# GROUNDDESC is split into two, because the item will be inserted between them
ITEMS = {
    'apple': {
        NAME: 'Apple',
        GROUNDDESC: ['An', 'sits on the ground'],
        SHORTDESC: 'a red apple',
        LONGDESC: 'This is a delicious fruit. Perhaps you can eat it.',
        PICKABLE: True,
        EDIBLE: True,
        TAG: 'food',
    },
    'cake': {
        NAME: 'Cake',
        GROUNDDESC: ['A tasty chocolate', 'is inside a box on the ground'],
        SHORTDESC: 'a tasty chocolate cake',
        LONGDESC: 'This delicious treat was baked with love, made from authentic chocolate chips',
        PICKABLE: True,
        PRICE: 10,
        EDIBLE: True,
        TAG: 'food',
    },
    'bread': {
        NAME: 'Bread',
        GROUNDDESC: ['A loaf of', 'sits on the ground'],
        SHORTDESC: 'a loaf of bread',
        LONGDESC: 'A tasty bread loaf, brown and crispy on the outside',
        PICKABLE: True,
        PRICE: 3,
        EDIBLE: True,
        TAG: 'food',
    },
    'beef': {
        NAME: 'Beef',
        GROUNDDESC: ['A cut of', 'lies in the dirt'],
        SHORTDESC: 'a cut of beef',
        LONGDESC: 'A raw piece of meat, it is tastier when cooked!',
        PICKABLE: True,
        PRICE: 35,
        EDIBLE: True,
        TAG: 'food',
    },
    'fountain': {
        NAME: 'Fountain',
        GROUNDDESC: ['A white', 'is streaming water'],
        SHORTDESC: 'a fabulous, stone fountain',
        LONGDESC: 'This beautiful sculpture is spraying water, attracting various kinds of birds.',
        PICKABLE: False,
        EDIBLE: False,
        TAG: 'decor',
    },
    'evergreen': {
        NAME: 'Evergreen',
        GROUNDDESC: ['A vibrant', 'rises from the earth'],
        SHORTDESC: 'a fragrant evergreen',
        LONGDESC: 'Deep green bristles erupt in a spire around this proud tree, fixed firmly in the ground.',
        PICKABLE: False,
        EDIBLE: False,
        TAG: 'decor',
    },
    'dagger': {
        NAME: 'Dagger',
        GROUNDDESC: ['A small', 'is thrown on the ground'],
        SHORTDESC: 'a small dagger',
        LONGDESC: 'This dagger, ancient and rusty as it is, is still sharp enough to be used as a weapon.',
        PICKABLE: True,
        EDIBLE: False,
        WEAPON: WEAPONS[DAGGER],
        TAG: 'weapon',
    },
    'sword': {
        NAME: 'Sword',
        GROUNDDESC: ['A long', 'is thrown on the ground'],
        SHORTDESC: 'a long, steel sword',
        LONGDESC: 'This sword is ancient. despite being forged from steel, ',
        PICKABLE: True,
        EDIBLE: False,
        WEAPON: WEAPONS[SWORD],
        SKILL: SKILLS[DOUBLETROUBLE],
        TAG: 'weapon',
    },
    'coin': {
        NAME: 'Coin',
        GROUNDDESC: ['A bronze', 'is dropped on the ground'],
        SHORTDESC: 'a bronze coin',
        LONGDESC: "This is a bronze coin, You can spend it at any shop in exchange for useful goods",
        PICKABLE: True,
        EDIBLE: False,
        TAG: 'coins',
    },
}