'''
Stores monster and related info
'''

from random import choice
from monsters import Monster

# stores monster adjectives and variations
MONSTER_VARIATION = ['Ruthless', 'Ferocious', 'Demonic',
                     'Brutal', 'Bloody', 'Violent', 'Wild', 'Spooky',
                     'Murderous', 'Fierce', 'Savage', 'Monsterous', 
                     'Hideous', 'Grotesque',
                    ]

# stores species names and their stats in a dictionary
MONSTER_SPECIES = {
    #Specie         |  NAME  | HP |  DMG  |  VERB  |
    'chicken':      ['Chicken', 1, 1,      'pinched'],
    'archer':       ['Archer', 1, 2,          'shot'],
    'spider':       ['Spider', 2, 1,           'hit'],
    'scorpion':     ['Scorpion', 1, 3,       'stung'],
    'guard':        ['Guard', 2, 2,        'punched'],
    'wolf':         ['Wolf', 3, 1,             'bit'],
    'werewolf':     ['Werewolf', 3, 2,         'bit'],
    'bear':         ['Bear', 4, 2,      'slashed at'],
    'knight':       ['Knight', 6, 3,        'jabbed'],
    'pbag':         ['Punching-Bag', 10, 0,       ''],
    'spbag':        ['Super-Punching-Bag', 999, 0,''],
}

# enemy combinations
# Different enemy arrangements
COMBAT_LEVELS = [
    ['spider', 'spider'],
    ['wolf', 'wolf'],
    ['guard', 'archer', 'wolf'],
    ['guard', 'guard', 'guard'],
    ['wolf', 'werewolf', 'wolf'],
    ['ogre', 'wolf'],
]

def give_monster(specie, special_name = False):
    '''
    given a species name, returns a monster object based on MONSTER_SPECIES dictionary
    '''
    mySpecieStats = MONSTER_SPECIES[specie]
    monsta = Monster(mySpecieStats[0], mySpecieStats[1], mySpecieStats[2], mySpecieStats[3])
    if special_name:
        # create name using MONSER_VARIATION
        adjective = choice(MONSTER_VARIATION)
        MONSTER_VARIATION.remove(adjective)
        monsta.name = '{} {}'.format(adjective,  monsta.name)
    return monsta
