'''
Contains various utility functions used to make the game flow.
'''
from dictionaries import *
from time import sleep
import os, platform

# Stores console's window size at launch
AC_SCREEN_WIDTH = 80
AC_SCREEN_HEIGHT = 35

# Console functions 
def set_console_size():
    '''
    Configures console's window size according to platform
    '''
    if platform.system() == 'Windows':
        os.system('title ASCII Combat')
        os.system('mode con: cols={} lines={}'.format(AC_SCREEN_WIDTH, AC_SCREEN_HEIGHT))
    elif platform.system() == 'Linux' or platform.system() == 'Darwin':
        os.system('echo -n -e "\033]0;ASCII Combat\007"')
        os.system('echo "\033[8;{};{}t"'.format(AC_SCREEN_HEIGHT, AC_SCREEN_WIDTH))

# ASCII functions 
def clear():
        '''
        Clears screen according to platform
        '''
        if platform.system() == 'Windows':
            os.system('cls')
        elif platform.system() == 'Linux' or platform.system() == 'Darwin':
            os.system('clear')

def pos(x, y):
    '''
    Returns an ANSI Sequence to change cursor position
    '''
    return '\x1b[{};{}H'.format(int(y), int(x))

def banner(text, corner='+', border='-'):
    '''
    Displays a banner, multi-lines are supported
    '''
    max_length = 0
    _text = text.split('\n')
    # Checks max line length
    for line in _text:
        if len(line) > max_length:
            max_length = len(line)
    sides = corner + border * max_length + corner
    final_text = [sides]
    for line in _text:
        dif = 0
        if len(line) != max_length:
            dif = max_length - len(line)
        final_text.append('|{}{}|'.format(line, ' ' * dif))
    final_text.append(sides)
    return '\n'.join(final_text)

def headline(text, char='='):
    '''
    Prints a headline
    '''
    print(text)
    print(len(text) * char)

def center_screen(text):
    '''
    Returns an empty screen with text in the middle
    '''
    final = ''
    wspan = AC_SCREEN_WIDTH - 2
    final += '+' + '-' * wspan + '+'
    lines = text.split('\n')
    no_of_newlines = AC_SCREEN_HEIGHT - (len(lines) + 2)
    no_of_topnewlines = int(no_of_newlines / 2)
    final += no_of_topnewlines * ('|' + ' ' * wspan + '|\n')
    for line in lines:
        lnt = (wspan - len(line)) // 2
        final += '|' + ' ' * lnt + line + ' ' * lnt
        final += '|\n'  if len(line) % 2 == 0 else ' |\n'
    no_of_botnewlines = no_of_newlines - no_of_topnewlines
    final += (no_of_botnewlines - 1) * ('|' + ' ' * wspan + '|\n')
    final += '|' + ' ' * wspan + '|'
    final += '+' + '-' * (AC_SCREEN_WIDTH-2) + '+'
    return final

def transition(time_in_seconds=3, text='Loading', phases=5):
    '''
    A transition between 2 scenes
    '''
    phase = 1
    while phase < phases + 1:
        clear()
        x = text + ' .' * phase + '\n'
        print(center_screen(x), end='')
        sleep(time_in_seconds / phases)
        phase += 1

def use_an(text, capitalize = False):
    '''
    True if text start with vowel and vice versa
    '''
    if text[0] in 'aeiou':
        a = 'an'
    else:
        a = 'a'
    if capitalize:
        a = list(a)
        a[0] = a[0].upper()
        a = ''.join(a)
    return a

def typewriter(text, speed=1):
    '''
    Simulates typing
    '''
    delay = 0.045 * speed
    for char in text:
        print(char, end='', flush=True)
        sleep(delay)
