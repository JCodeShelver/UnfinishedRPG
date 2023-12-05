import sys
import time
import random

from Utils import sprint

def altBattle(stage: int,  enemy):
    enemy['lvl'] = random.randint(enemy['lvlRange'][0], enemy['lvlRange'][1])
    if enemy['lvl'] > (stage + 9):
        enemy['lvl'] = (stage + 9)
    elif enemy is ice_sorceress:
        enemy['stats']['hp'] = enemy['lvl'] * 50
    elif enemy is iron_knight:
        enemy['stats']['hp'] = enemy['lvl'] * 2
    elif enemy is golem:
        enemy['stats']['hp'] += enemy['lvl'] * 8
    elif enemy is arrow_master:
        enemy['stats']['hp'] += enemy['lvl'] * 37500

    sprint(f'A(n) {enemy["name"]} challenges you!\n')

from AlternateDefaultHero import altPlayer #as altPlayer
from SaveLoad import *
from AlternateEnemyList import *

sprint('Entering the tournament...\n')
time.sleep(1.5)
sprint('You arrive at the tournament.\nYou proceed to the first stage.\n')
altPlayer['stage'] = 1
altBattle(1, ice_sorceress)
