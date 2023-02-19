'''
Stores constants needed for dictionary files to work as intended.
Stores window size and tags to be displayed in inventory, bullets,
and separators and dictionary keys
'''


# list of tags displayed in inventory
INVENTORY_TAGS = ['food', 'weapon', 'armor'] 
# max number of items that can be found in a room
GROUND_LIMIT = 5
# text constants
BULLET = '  > '
SEP = ' * ' # --> ●
FILLBAR = '█'
EMPTYBAR = '░'
# weapon dictionary keys
FIST = 'fist'
DAGGER = 'dagger'
SWORD = 'sword'
BOW = 'bow'
VERB = 'verb'
# skill dictionary keys
FUNCTION = 'function'
DMG = 'dmg'
MESSAGE = 'message'
ISMULTI = 'ismulti'
DOUBLETROUBLE = 'doubletrouble'
ARROWSTORM = 'arrowstorm'
# room/item dictionary keys
NAME = 'name'
USERDESC = 'userdesc'
DESC = 'desc'
NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'
UP = 'up'
DOWN = 'down'
GROUND = 'ground'
SHOP = 'shop'
SHOPINTRO = 'shopintro'
ENEMIES = 'enemies'
SEEN = 'seen'
DIRECTIONS = [NORTH, SOUTH, EAST, WEST, UP, DOWN]
# item dictionary keys
GROUNDDESC = 'grounddesc'
SHORTDESC = 'shortdesc'
LONGDESC = 'longdesc'
PICKABLE = 'pickable'
PRICE = 'price'
EDIBLE = 'edible'
WEAPON = 'weapon'
SKILL = 'skill'
TAG = 'tag' # Tags can be food, weapon, random, decor
