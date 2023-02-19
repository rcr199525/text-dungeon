'''
"Main" module that launches the game and stats the cmdloop()
'''

from dictionaries.weapon_skills import *
from dictionaries.rooms import *
from dictionaries.utils import *
from dictionaries.monsters import give_monster
import combat, dungeon, sys

def main():
    sys.path.append(os.getcwd())
    set_console_size()
    me = Player('Steve', 10, WEAPONS[SWORD])
    enemies = [give_monster('wolf') for i in range(3)]

    # Comment/Uncomment game/world depending on which one you want to try

    # world is the dungeon system, game is the combat system, they are not
    # joined together yet, untill then this what you can do
    world = dungeon.Dungeon(me, ROOMS)
    world.cmdloop()
    # game = combat.Combat(me, enemies)
    # game.cmdloop()

if __name__ == '__main__':
    main()  


