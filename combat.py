'''
Instantiate this to create a Combat 'scene' containing a player and enemies
both must be given, run the Combat.cmdloop() to start the scene
'''
from monsters import Monster
from dictionaries.utils import *
import cmd, platform, os
from time import sleep
from random import randint

class Combat(cmd.Cmd):
    STRINGS = {
    'intro'        : 'You choose to fight. Enemies are staring viciously at you!\nPress Enter to start . . .',
    'win'          : 'VICTORY, You defeated all enemies!\nPress Enter to Exit . . .',
    'lose'         : 'DEFEAT, You got beaten by enemies!\nPress Enter to Exit . . .',
    'syntax_error' : 'Oops! I dont understand',
    'unknown_enemy': "I can't see that enemy!",
    'enemy_death'  : "You eliminated",
    'user_death'   : "You are bleeding too much.. Argh!",
    'full_hp'      : "You are perfectly healthy!",
    'prompt'       : 'Type <atk> to attack:\n> ',
    'prompt_skl'   : 'Type <atk> or <skl>:\n> ',
    'atk_choice'   : 'Attack .. Choose enemy number:\n',
    'skl_choice'   : 'Skill  .. Choose enemy number:\n',
    'no_skl'       : "Oops! It seems like you haven't acquired a skill yet!",
    'no_pwr'       : 'Oops! not enough power to use your skill!',
    }

    # Global constants
    LIST_SYMBOL = '  *'
    PROMPT_SIGN = '# '

    def __init__(self, user, enemies):
        '''# cmd.Cmd initialization'''
        super().__init__()
        # Color settings
        self.intro = input(center_screen(self.STRINGS['intro']))
        self.prompt = '{}{}'.format(self.PROMPT_SIGN, self.STRINGS['prompt'])
        # user/enemies variables
        self.user = user
        self.STRINGS['player_attack'] = 'You ' + self.user.weapon_verb
        self.user_attack_msg = ''
        self.enemies = enemies
        self.no_of_enemies = len(enemies)
        self.enemies_dict = self.create_dictionary()
        self.enemies_attack_msg = ''

    # cmd.Cmd method overriding
    def emptyline(self):
        '''Avoids repitition of last command'''
        self.display()
        pass

    def default(self, line):
        '''Error message for unknown commands'''
        self.display()
        print('{}{} <{}>'.format(self.PROMPT_SIGN, self.STRINGS['syntax_error'], line))
        print('', end='')

    def do_help(self, arg):
        '''Removes the help method'''
        self.display()
        pass

    def postcmd(self, stop, line):
        '''Controls termination of Combat, win/lose msg'''
        # Checks win condition
        if not self.enemies_alive():
            print(self.PROMPT_SIGN + self.STRINGS['win'], end='')
            input()
            return True
        elif self.enemies_alive() and not self.user.alive:
            print(self.PROMPT_SIGN + self.STRINGS['lose'], end='')
            input()
            return True
        # Changes prompt if Skill is available to use
        if self.user.skill == self.user.max_skill:
            self.prompt = self.PROMPT_SIGN + self.STRINGS['prompt_skl']
        else: 
            self.prompt = self.PROMPT_SIGN + self.STRINGS['prompt']

    # Pre/Post Loop functions
    def preloop(self):
        self.display()
   
    def postloop(self):
        pass

    @staticmethod
    def reset_color():
        print('', end='')

    # ENEMIES, PLAYER, COMBAT STUFF
    def create_dictionary(self):
        '''Creates a dictionary that store Enemies and their corresponding names'''
        dict = {}
        counter = 1
        for enemy in self.enemies:
            if enemy.alive:
                dict[str(counter)] = enemy
                counter += 1
        return dict
    
    def alive_enemy_names(self):
        '''Returns a string of alive enemy names'''
        names = ''
        counter = 1
        for enemy in self.enemies:
            if enemy.alive:
                names += '  {}| {}\n'.format(counter, enemy.name)
                counter += 1
        return names

    def enemies_alive(self):
        '''Are any enemy alive? True/False'''
        self.no_of_enemies = len(self.enemies)
        for enemy in self.enemies:
            if not enemy.alive:
                self.no_of_enemies -= 1
        if self.no_of_enemies > 0:
            return True
        else:
            return False
        
    def enemy_death_msg(self, enemy, dmg_taken):
        '''Checks if enemy will die from a specific blow and returns a string accordingly'''
        if (enemy.hp - dmg_taken) <= 0:
            # Message if enemy is dead
            outcome = "\n{}{} {}".format(self.PROMPT_SIGN, self.STRINGS['enemy_death'], enemy.name)
        else:
            outcome = ''
        return outcome

    def user_attack(self, enemy):
        '''Attacks a chosen enemy'''
        self.user_attack_msg = "{}{} {} (-{}HP)".format(self.PROMPT_SIGN, self.STRINGS['player_attack'], enemy.name, self.user.dmg)
        self.user_attack_msg += self.enemy_death_msg(enemy, self.user.dmg)
        self.user.attack(enemy)

    def user_skill(self, enemies):
        '''Attacks enemy using the player's current skill'''
        my_skill = self.user.skill_type
        # Executes skill depending multi-target/single-target skill
        if my_skill['ismulti']:
            self.user_attack_msg = ("{}SKILL: {} >>>\n{} (-{}HP to all)".format(self.PROMPT_SIGN, my_skill['name'].upper(),
            my_skill['message'], my_skill['dmg']))
            for enemy in enemies:
                self.user_attack_msg += self.enemy_death_msg(enemy, my_skill['dmg'])
            my_skill['function'](self.user, enemies)
        else:
            self.user_attack_msg = ("{}SKILL: {} >>>\n{} {} {} (-{}HP)".format(self.PROMPT_SIGN, my_skill['name'].upper(), 
            self.STRINGS['player_attack'], enemies.name, my_skill['message'], my_skill['dmg']))
            self.user_attack_msg += self.enemy_death_msg(enemies, my_skill['dmg'])
            my_skill['function'](self.user, enemies)
        self.user.skill = 0

    def enemies_attack(self):
        '''All alive enemies attacks the user and returns a hit string'''
        messages = ''
        for enemy in self.enemies:
            if enemy.alive:
                if enemy.dmg == 0:
                    hit_string = ''
                else:
                    enemy.attack(self.user)
                    hit_string = "!! {} {} you (-{}HP)\n".format(enemy.name, enemy.action, str(enemy.dmg))
                messages += hit_string
        if self.user.hp <= 0:
            messages += self.PROMPT_SIGN + self.STRINGS['user_death']
        elif self.user.hp == self.user.max_hp:
            messages += self.PROMPT_SIGN + self.STRINGS['full_hp']
        else:
            messages += 'You survived enemy attacks with {}/{} HP left'.format(self.PROMPT_SIGN, self.user.hp, self.user.max_hp)
        self.enemies_attack_msg = messages

    # UTILITY FUNCTIONS   
    def display(self, clr = True):
        '''Displays the interface: All Enemies and user status'''
        self.reset_color()
        if clr:
            clear()
        self.user.show()
        for enemy in self.enemies:
            if enemy.alive:
                print(enemy.show())
            else:
                print(enemy.show())
                self.reset_color()
        print()
        # Reveals events slowly
        if self.user_attack_msg:
            for line in self.user_attack_msg.split('\n'):
                sleep(0.5)
                print(line)
        if self.enemies_attack_msg:
            for line in self.enemies_attack_msg.split('\n'):
                sleep(0.75)
                print(line)
        self.user_attack_msg = ''
        self.enemies_attack_msg = ''
        # print(self.enemies_attack_msg)
        print('')

    def error_msg(self, text):
        '''A wrapper for printing an error message'''
        self.display()
        print(self.PROMPT_SIGN + text)

    def demand_and_execute(self, function, _prompt=STRINGS['atk_choice']):
        '''
        A loop that executes any given function on an enemy whenever a valid input is entered
        '''
        self.display()
        while True:
            choice = input(self.PROMPT_SIGN + _prompt + self.alive_enemy_names() + '> ')
            self.enemies_dict = self.create_dictionary()
            try:
                target_enemy = self.enemies_dict[choice.lower()]
                function(target_enemy)
                self.enemies_attack()
                self.display()
                return True
            except KeyError:
                print('', end='')
                input(self.PROMPT_SIGN + self.STRINGS['unknown_enemy'])
                self.display()

    # USER INPUT AND COMMANDS
    # Cmd commands
    def do_atk(self, arg):
        """Attacks a specific enemy, type <atk>"""
        self.demand_and_execute(self.user_attack)

    def do_skl(self, arg):
        """Unleashs special power using up all power points, type <skl>"""
        if self.user.skill_type == None:
            self.error_msg(self.STRINGS['no_skl'])
        elif self.user.skill == self.user.max_skill:
            # Multi and single target skill execution
            if not self.user.skill_type['ismulti']:
                self.demand_and_execute(self.user_skill, self.STRINGS['skl_choice'])
            else:
                enemies_list = []
                for enemy in self.enemies:
                    if enemy.alive:
                        enemies_list.append(enemy)
                self.user_skill(enemies_list)
                self.enemies_attack()
                self.display()
        else:
            self.error_msg(self.STRINGS['no_pwr'])
