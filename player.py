'''
A Player class, every player got: HP, DMG, WEAPON and a SKILL
'''

from dictionaries import weapon_skills as ws
from dictionaries.weapon_skills import *
from monsters import Monster

class Player(Monster):
    def __init__(self, name, hp, weapon):
        super().__init__(name, hp, weapon[DMG])
        # Sets skills dmg
        ws.set_skills_dmg(self.dmg)
        self.weapon = weapon
        self.weapon_verb = self.weapon[VERB]
        self.enemies = []
        self.skill_type = ws.SKILLS[weapon[SKILL]]
        self.skill = 0
        self.max_skill = 3

    def show(self, size='max'):
        '''Displays user stats'''
        print('>', self.name)
        if self.alive:
            print('* HP     |' + '█' * self.hp + '░' * (self.max_hp - self.hp) + ' ' + str(self.hp))
        print('* Weapon |' + '{} (DMG: {})'.format(self.weapon[NAME], self.dmg))
        print('* Skill  |' + '{}'.format(self.skill_type['name']))
        pwr_string = '* Power  |' + ('*' * self.skill) + 'o' * (self.max_skill - self.skill)
        if self.skill == self.max_skill:
            print(pwr_string + ' (Ready!)')
        else:
            print(pwr_string)

    def attack(self, enemy):
        '''attacks specified enemy'''
        super().attack(enemy)
        if self.skill < self.max_skill:
            self.skill += 1

    # Skill functions
    def double_trouble(self, enemy):
        '''performs double trouble skill on specified enemy'''
        enemy.hp -= ws.SKILLS[DOUBLETROUBLE]['dmg']
        enemy.update_data()

    def arrow_storm(self, enemies):
        '''performs arrow storm skill on specified enemy'''
        for enemy in enemies:
            enemy.hp -= ws.SKILLS[ARROWSTORM]['dmg']
            enemy.update_data()
