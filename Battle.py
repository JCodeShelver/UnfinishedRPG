import random
import sys
import time
from Utils import sprint
from DefaultHero import player as player
from LevelUp import level as level
from EnemyList import *
from SaveLoad import *

def playerTakeDmg(attacker, defender):
    dmg = random.randint(attacker['stats']['atk'][0], \
                         attacker['stats']['atk'][1])
    defender['stats']['hp'] -= dmg
    if defender['stats']['hp'] <= 0:
        sprint(f'{defender["name"]} has been slain.\n')
        if defender == player:
            sprint('You died!\n')
            sprint('Would you like to continue? Y/N ')
            gameover = input().lower()
            if gameover == 'y':
                load()
            if gameover == 'n':
                sprint('Game Over!\n')
                time.sleep(5)
                sys.exit()
    sprint(f'{defender["name"]} takes {dmg} damage!\n')
    commands(defender, attacker)

def takeDmgextra(attacker, defender):
    dmgprecursor = random.randint(attacker['stats']['atk'][0], \
                         attacker['stats']['atk'][1])
    dmg = (1 + random.randint(attacker['atkplus'][0], attacker['atkplus'][1]) / 100) * dmgprecursor
    defender['stats']['hp'] -= dmg
    if defender['stats']['hp'] <= 0:
        sprint(f'{defender["name"]} has been slain.\n')
        if defender == player:
            sprint('You died!\n')
            sprint('Would you like to continue? Y/N ')
            gameover = input().lower()
            if gameover == 'y':
                load()
            elif gameover == 'n':
                sprint('Game Over!\n')
                time.sleep(5)
                sys.exit()
    sprint(f'{defender["name"]} takes {dmg} damage!\n')
    commands(defender, attacker)

def enemyTakeDmg(attacker, defender):
    atks = '\n'.join(sorted(attacker['ratks'])+ sorted(attacker['aatks']) + sorted(attacker['satks']) + sorted(attacker['matks']))
    sprint(atks)
    sprint('Choose your attack: ')
    dmg = input()
    if dmg == 'r1':
        dmg = random.randint(((attacker['stats'][0] * attacker['stats']['str'])/2.3), \
                             ((attacker['stats'][1] * attacker['stats']['str'])/2.3))
    if dmg == 'r2':
        dmg = random.randint(((attacker['stats'][0] * attacker['stats']['str'] / 2 * attacker['stats']['dex'])/1.7), \
                             ((attacker['stats'][1] * attacker['stats']['str'] / 2 * attacker['stats']['dex'])/1.7))
    if dmg == 'r3':
         dmg = random.randint(((attacker['stats'][0] * attacker['stats']['str'])/3.8), \
                             ((attacker['stats'][1] * attacker['stats']['str'])/3.8))
    if dmg == 'r4' and attacker['ratks']['4'] != 'locked':
        pass
    if dmg == 'r5' and attacker['ratks']['5'] != 'locked':
        pass
    if dmg == 'r6' and attacker['ratks']['6'] != 'locked':
        pass
    if dmg == 'a1' and attacker['aatks']['1'] != 'locked':
        pass
    if dmg == 'a2' and attacker['aatks']['2'] != 'locked':
        pass
    if dmg == 'a3' and attacker['aatks']['3'] != 'locked':
        pass
    if dmg == 'a4' and attacker['aatks']['4'] != 'locked':
        pass
    if dmg == 's1' and attacker['satks']['1'] != 'locked':
        pass
    if dmg == 's2' and attacker['satks']['2'] != 'locked':
        pass
    if dmg == 's3' and attacker['satks']['3'] != 'locked':
        pass
    if dmg == 'm1' and attacker['matks']['1'] != 'locked':
        pass
    defender['stats']['hp'] -= dmg
    if defender['stats']['hp'] <= 0:
        sprint(f'{defender["name"]} has been slain.\n')
        if defender == player:
            sprint('You died!\n')
            sprint('Would you like to continue? Y/N ')
            gameover = input().lower()
            if gameover == 'y':
                load()
            if gameover == 'n':
                sprint('Game Over!\n')
                time.sleep(5)
                sys.exit()
        if attacker == player:
            if defender == ghost:
                if attacker['pets']['slot1'] == 'empty':
                        attacker['pets']['slot1'] = defender['reward']
                        sprint(f'You\'ve obtained {defender["reward"]}!\n')
                if attacker['pets']['slot1'] != 'empty':
                    for slots in attacker['pets']:
                        for slot in slots:
                            if slot == 'empty':
                                slot = defender['reward']
                    sprint(f'You\'ve obtained {defender["reward"]}!\n')
                    attacker['xp'] += defender['xpreward']
                    level(attacker)
            elif defender == dragon:
                    if attacker['items']['slot1'] == 'empty':
                        random.shuffle(dragon['reward'])
                        attacker['items']['slot1'] = defender['reward'][0]
                        sprint(f'You\'ve obtained {defender["reward"[0]]}!\n')
                    if attacker['items']['slot1'] != 'empty':
                        for slots in attacker['items']:
                            for slot in slots:
                                if slot == 'empty':
                                    slot = defender['reward']
                        sprint(f'You\'ve obtained {defender["reward"]}!\n')
                        attacker['xp'] += defender['xpreward']
                        level(attacker)
            if attacker['items']['slot1'] == 'empty':
                attacker['items']['slot1'] = defender['reward']
                sprint(f'You\'ve obtained {defender["reward"]}!\n')
            for slots in attacker['items']:
                for slot in slots:
                    if slot == 'empty':
                        slot = defender['reward']
            sprint(f'You\'ve obtained {defender["reward"]}!\n')
            attacker['xp'] += defender['xpreward']
            level(attacker)
    else:
        sprint(f'{defender["name"]} takes {dmg} damage!\n')
        commands(attacker, defender)

def commands(knight, enemy):
    sprint(f'You\'ve run into a(n) {enemy["name"]}!!!\n')
    a=0
    while a != 5:
        sprint('-------------------\n')
        sprint('Do you want to attack?\nIf not, you can choose to cast a spell. Y/')
        attack = input('N ').lower()
        if 'y' in attack:
            enemyTakeDmg(knight, enemy)
            a += 1
        elif 'n' in attack:
            sprint('Do you want to cast a spell? Y/')
            spell = input('N ').lower()
            if 'y' in spell:
                spells(knight['stats']['int'])
            if 'n' in spell:
                sprint(f'{enemy["name"]} takes the opportunity to attack {knight["name"]}!\n')
                playerTakeDmg(enemy, knight)
        else:
            commands(knight, enemy)
    while True:
        if a == 5:
            sprint(f'{enemy["name"]} takes the opportunity to attack the {knight["name"]} with extra power!\n')
            takeDmgextra(enemy, knight)

#

def spells(knowledge: int): #activate with "spells(player['stats']['int'])
    def heal(amt: int):
        from math import ceil
        if player['stats']['hp'] == player['stats']['maxHp']:
                    sprint('You are already fully healed!')
        else:
            player['stats']['str'] -= ceil(amt / 2)
            player['stats']['hp'] += amt
            if player['stats']['hp'] > player['stats']['maxHp']:
                player['stats']['hp'] = player['stats']['maxHp']

    if knowledge >= 25:
        sprint('Would you like to cast a heal, power, or money spell')
        cast = input("? ").lower()
        if cast == 'yes':
            sprint('Power, Money, or Heal')
            choose = input('? ').lower()
            if choose == 'power':
                player["stats"]['str'] += 10
                player['stats']['atk'][1] += 5
                player['stats']['hp'] -= 20
            elif choose == 'heal':
                heal(10)
            elif choose == 'money':
                player['stats']['str'] -= 5
                player['stats']['dex'] -= 5
                amount = random.randint(5 * player['lvl'], 10 * player['lvl'])
                currencies = ['jewels', 'crowns', 'doubloons']
                random.shuffle(currencies)
                player['stats'][currencies[0]] += amount
    elif knowledge >= 10:
        sprint('Would you like to cast a heal or power spell? ')
        cast = input().lower()
        if cast == 'yes' or cast == 'y':
            sprint('Power or Heal? ')
            choose = input().lower()
            if choose == 'power':
                player["stats"]['str'] += 5
                player['stats']['atk'][1] += 3
                player['stats']['hp'] -= 10
            elif choose == 'heal':
                heal(1)
    elif knowledge >= 5:
        sprint('Would you like to cast a basic heal spell? ')
        cast = input().lower()
        if cast == 'yes' or cast == 'y':
            heal(1)
    sprint(player['stats'])