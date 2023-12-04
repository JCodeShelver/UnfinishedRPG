import sys
import time
import random

def sprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)

from typing import Dict, Any

def altBattle(stage: int,  enemy: Dict[str, Any]):
    enemy['lvl'] = random.randint(enemy['lvlRange'][0], enemy['lvlRange'][1])
    if enemy['lvl'] > (stage + 9):
        enemy['lvl'] = (stage + 9)
    if enemy['name'] == 'Ice sorceress':
        enemy['stats']['hp'] = enemy['lvl'] * 50
    if enemy['name'] == 'Iron knight':
        enemy['stats']['hp'] = enemy['lvl'] * 2
    if enemy['name'] == 'Gem golem':
        enemy['stats']['hp'] += enemy['lvl'] * 8
    if enemy['name'] == 'Archer of Fate':
        enemy['stats']['hp'] += enemy['lvl'] * 37500
    sprint(f'A(n) {enemy["name"]} challenges you!\n')

from AlternateDefaultHero import *
from SaveLoad import *
from AlternateEnemyList import *

sprint('Entering the tournament...\n')
time.sleep(1.5)
sprint('You arrive at the tournament.\nYou proceed to the first stage.\n')
altPlayer['stage'] = 1
altBattle(1, ice_sorceress)
