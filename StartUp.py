import os
import pickle
import random
import sys
import time
with open('mDoc.dat', 'rb') as m:
    megaGems=pickle.load(m)
dlcCost = {'legend armor' : 7500,
           'resurrection spell recipe' : 5000}
def sprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)

#-------Map Layout-------#

zone1 = {
    'a1': {
        'name':'Home',
        'description':'This is the home you live in.',
        'solved':False,
        'up':'',
        'down':['down', 'south'],
        'left':'',
        'right':['right', 'east']},
    'a2': {
        'name':'Town Outskirts',
        'description':'The outer parts of the town.',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':'',
        'right':['right', 'east']},
    'a3': {
        'name':'Town Plaza',
        'description':'This is the majority of the city.',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':'',
        'right':['right', 'east']},
    'a4': {
        'name':'Town Market',
        'description':'This is the market, the local shops.',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':'',
        'right':['right', 'east']},
    'a5': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':'',
        'left':'',
        'right':['right', 'east']},
    'b1': {
        'name':'',
        'description':'',
        'solved':False,
        'up':'',
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'b2': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'b3': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'b4': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'b5': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':'',
        'left':['left', 'west'],
        'right':['right', 'east']},
    'c1': {
        'name':'',
        'description':'',
        'solved':False,
        'up':'',
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'c2': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'c3': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'c4': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'c5': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':'',
        'left':['left', 'west'],
        'right':['right', 'east']},
    'd1': {
        'name':'',
        'description':'',
        'solved':False,
        'up':'',
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'd2': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'd3': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'd4': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':['right', 'east']},
    'd5': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':'',
        'left':['left', 'west'],
        'right':['right', 'east']},
    'e1': {
        'name':'',
        'description':'',
        'solved':False,
        'up':'',
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':''},
    'e2': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':''},
    'e3': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':''},
    'e4': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':['down', 'south'],
        'left':['left', 'west'],
        'right':''},
    'e5': {
        'name':'',
        'description':'',
        'solved':False,
        'up':['up', 'north'],
        'down':'',
        'left':['left', 'west'],
        'right':''}}

def atkUnlocks(pLvl):               #enter 'player['lvl'] or hero['lvl']
    if pLvl >= 100:
        player['matks']['1'] = 'supernova'
        player['ratks']['4'] = 'theknee'
        player['ratks']['5'] = 'roundhousekick'
        player['aatks']['1'] = 'bullrage'
        player['satks']['1'] = 'swordslicers'
        player['aatks']['2'] = 'sciencegleam'
        player['ratks']['6'] = 'elementalball'
        player['aatks']['3'] = 'swordoflight'
        sprint ('You unlocked your first mega attack, supernova!\n')
        sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        sprint ('You unlocked your first special attack, sword slicers!\n')
        sprint ('You unlocked science gleam!\n')
        sprint ('You unlocked the elemental ball, and the sword of light!\n')
    elif pLvl >= 50:
        player['ratks']['4'] = 'theknee'
        player['ratks']['5'] = 'roundhousekick'
        player['aatks']['1'] = 'bullrage'
        player['satks']['1'] = 'swordslicers'
        player['aatks']['2'] = 'sciencegleam'
        player['ratks']['6'] = 'elementalball'
        player['aatks']['3'] = 'swordoflight'
        sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        sprint ('You unlocked your first special attack, sword slicers!\n')
        sprint ('You unlocked science gleam!\n')
        sprint ('You unlocked the elemental ball, and the sword of light!\n')
    elif pLvl >= 30:
        player['ratks']['4'] = 'theknee'
        player['ratks']['5'] = 'roundhousekick'
        player['aatks']['1'] = 'bullrage'
        player['satks']['1'] = 'swordslicers'
        player['aatks']['2'] = 'sciencegleam'
        sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        sprint ('You unlocked your first special attack, sword slicers!\n')
        sprint ('You unlocked science gleam!\n')
    elif pLvl >= 25:
        player['ratks']['4'] = 'theknee'
        player['ratks']['5'] = 'roundhousekick'
        player['aatks']['1'] = 'bullrage'
        player['satks']['1'] = 'swordslicers'
        sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        sprint ('You unlocked your first special attack, sword slicers!\n')
    elif pLvl >= 10:
        player['ratks']['4'] = 'theknee'
        player['ratks']['5'] = 'roundhousekick'
        player['aatks']['1'] = 'bullrage'
        sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
    elif pLvl >= 5:
        player['ratks']['4'] = 'theknee'
        sprint ('You unlocked the knee attack!\n')

def level(pStats, mode=0):                  #enter 'player' or 'hero' inside of peremeter 1, mode perameter is a secret
    if mode==0:
        if pStats['lvl'] > 250:
            pStats['lvl'] = 250
            pStats['xp'] = -1
            pStats['lvlNext'] = -1
        elif pStats['lvl'] == 250:
            sprint('Sorry, you are already at the max level.\n')
        else:
            nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, [0, 0]
            while pStats['xp'] >= pStats['lvlNext'] and pStats['lvl'] <= 250:
                pStats['lvl'] += 1
                pStats['xp'] -= pStats['lvlNext']
                pStats['lvlNext'] = round(pStats['lvlNext'] * 1.5)
                nStr += 1
                nDex += 1
                nInt += 1
                nMag += 1
                nAtkDmg = [(round(pStats['stats']['atk'][0] * 3.7)), (round(pStats['stats']['atk'][1] * 3.7))]
                nMaxHp = round(pStats['stats']['maxHp'] * 2.2)
                nHp = nMaxHp
            if pStats['lvl'] >= 250:
                pStats['lvl'] = 250
                pStats['xp'] = -1
                pStats['lvlNext'] = -1
                sprint(f'You have reached the max level! Congratulations, {pStats["name"]}!\n')
            sprint(f'Level: {pStats["lvl"]}')
            sprint(f'Exp: {pStats["xp"]}')
            sprint(f'Stats: STRENGTH {pStats["stats"]["str"]} +{nStr}, \
                   DEXTERITY {pStats["stats"]["dex"]} +{nDex}, \
                   INTELLIGENCE {pStats["stats"]["int"]} +{nInt}, \
                   HEALTH {pStats["stats"]["hp"]} +{nHp}, \
                   ATTACK {pStats["stats"]["atk"][0]}, {pStats["stats"]["atk"][1]} +{nAtkDmg[0]}, {nAtkDmg[1]}, \
                   MAGIC {pStats["stats"]["mag"]} +{nMag}\n')
            pStats['stats']['atk'][0] += nAtkDmg[0]
            pStats['stats']['atk'][1] += nAtkDmg[1]
            pStats['stats']['hp'] += nHp
            pStats['stats']['maxHp'] += nMaxHp
            pStats['stats']['str'] += nStr
            pStats['stats']['dex'] += nDex
            pStats['stats']['int'] += nInt
            pStats['stats']['mag'] += nMag
            sprint(f'Exp left required to gain a level:\n {pStats["lvlNext"] - pStats["xp"]}')
            sprint(f'Exp required total to gain level:\n {pStats["lvlNext"]}')
            nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, [0, 0]
            sprint('------------------------------\n')
            atkUnlocks(pStats['lvl'])
    elif mode==1:
        nStr, nDex, nInt, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0

        while pStats['xp'] >= pStats['lvlNext']:
            pStats['lvl'] += 1
            pStats['xp'] -= pStats['lvlNext']
            pStats['lvlNext'] = round(pStats['lvlNext'] * 2)
            nStr += 1.5
            nDex += 1.5
            nInt += 1.5
            nAtkDmg = [(round(pStats['stats']['atk'][0] * 4.2)), (round(pStats['stats']['atk'][1] * 4.2))]
            nMaxHp = round(pStats['stats']['maxHp'] * 3)
            nHp = nMaxHp
            sprint(f'Level: {pStats["lvl"]}')
            sprint(f'\nExp: {pStats["xp"]}')
            sprint('\nStats:\n    Str:', nStr, '\n     Dex:', nDex, '\n     Int:', nInt, '\n     Health:', nHp, '\n     Atk:\n        ', nAtkDmg[0], '-', nAtkDmg[1])
            pStats['stats']['atk'][0] += nAtkDmg[0]
            pStats['stats']['atk'][1] += nAtkDmg[1]
            pStats['stats']['hp'] += nHp
            pStats['stats']['maxHp'] += nMaxHp
            pStats['stats']['str'] += nStr
            pStats['stats']['dex'] += nDex
            pStats['stats']['int'] += nInt
            nStr, nDex, nInt, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0
    elif mode==2:
        pass

def save():
    if os.path.isfile('do-not-touch.dat') == False:
        with open('do-not-touch.dat', 'wb') as f:
            pickle.dump(hero, f)
            print ("\nGame has been saved!\n")
    else:
        if os.path.isfile('do-not-touch(1).dat') == False:
            with open('do-not-touch(1).dat', 'wb') as f:
                pickle.dump(hero, f)
                print ("\nGame has been saved!\n")
        elif os.path.isfile('do-not-touch(2).dat') == False:
            with open('do-not-touch(2).dat', 'wb') as f:
                pickle.dump(hero, f)
                print ("\nGame has been saved!\n")
        elif os.path.isfile('do-not-touch(3).dat') == False:
            with open('do-not-touch(3).dat', 'wb') as f:
                pickle.dump(hero, f)
                print ("\nGame has been saved!\n")

def load():
    save = input('What save file would you like to load?\n1\n2\n3\n4\n> ')
    try:
        if save == "1" and os.path.isfile('do-not-touch.dat'):
            with open('do-not-touch.dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "2" and os.path.isfile('do-not-touch(1).dat'):
            with open('do-not-touch(1).dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "3" and os.path.isfile('do-not-touch(2).dat'):
            with open('do-not-touch(2).dat', 'rb') as f:
                player = pickle.dump(f)
                print ("\nGame has been loaded!\n")
        elif save == "4" and os.path.isfile('do-not-touch(3).dat'):
            with open('do-not-touch(3).dat', 'rb') as f:
                player = pickle.dump(f)
                print ("\nGame has been loaded!\n")
    except FileNotFoundError:
        print('Save file not located! Try to load a different file.')


imp = {'name' : 'Imp',
      'lvl' : [1, 8], #level
      'atkplus' : [3, 11], # %boost on atk
      'reward' : 'a Molten tongue', #reward for slaying
      'xpreward' : [2, 14],
      'stats' : {'str' : 3, #strength
             'dex' : 1, #dexterity or skill
             'int' : 2, #intelligence
#            'hp' : 3-24, depend on lvl
                 'atk' : [5, 13]}} #attack power
iron_knight = {'name' : 'Iron knight',
      'lvl' : [7, 18], #level
      'atkplus' : [9, 14], # %boost on atk
      'reward' : 'the Knight\'s armor', #reward for slaying
      'xpreward' : [20, 51],
      'stats' : {'str' : 18, #strength
             'dex' : 14, #dexterity or skill
             'int' : 6, #intelligence
#            'hp' : 35-90 depend on lvl
             'atk' : [14, 31]}} #attack power
cyclop = {'name' : 'Cyclops',
      'lvl' : [4, 9],  #level
      'atkplus' : [5, 16], # %boost on atk
      'reward' : 'a Cyclops eye', #reward for slaying
      'xpreward' : [12, 15],
      'stats' : {'str' : 12, #strength
             'dex' : 5, #dexterity or skill
             'int' : 3, #intelligence
#            'hp' : 24-54 #health
             'atk' : [9, 15]}} #attack power
dragon = {'name' : 'Golden dragon',
      'lvl' : 40, #level
      'atkplus' : [40, 65], # %boost on atk
      'reward' : ['Gold dragon wings', 'a Gold dragon pelt',\
                  'a set of Gold dragon armor'], #reward for slaying
      'xpreward' : [5000, 12000],
      'stats' : {'str' : 605, #strength
             'dex' : 20, #dexterity or skill
             'int' : 50, #intelligence
             'hp' : 30000, #health
             'atk' : [5250, 6750]}} #attack power
ghost = {'name' : 'Legendary ghoul',
      'lvl' : 10.5, #level
      'atkplus' : [7, 13], # %boost on atk
      'reward' : 'Ghost doggie', #reward for slaying
      'xpreward' : [30, 30.5],
      'stats' : {'str' : 7, #strength
             'dex' : 0, #dexterity or skill
             'int' : 5, #intelligence
             'hp' : 25, #health
             'atk' : [14, 23]}} #attack power
arrow_master = {'name' : 'Archer of Fate',
      'lvl' : 50, #level
      'atkplus' : [10, 40], # %boost on atk
      'reward' : 'a new special attack', #reward for slaying
      'xpreward' : [10000, 15000],
      'stats' : {'str' : 5000, #strength
             'dex' : 500, #dexterity or skill
             'int' : 500, #intelligence
             'hp' : 75000,
             'atk' : [500, 700]}} #attack power

#-------Default Player (gets overrided if user loads a game)-------#
player = {'lvl' : 1, #level
        'xp' : 0, # experience
        'name' : 'bob',
        'lvlNext' : 25, #xp goal to next lvl
        'location' : '',
        'savefile' : 0,
        'role' : 'unaffiliated',
        'stats' : {'str' : 1, #strength
            'dex' : 1, #dexterity or skill
            'int' : 1, #intelligence
            'mag' : 1, #magic
            'hp' : 30, #current health
            'maxHp': 30, #maximum health
            'speed' : 1,
            'luck' : 1,
            'crowns' : 10,
            'doubloons' : 0,
            'jewels' : 0,
            'atk' : [2, 12]},
        'items' : {'slot1' : 'empty',
            'slot2' : 'empty',
            'slot3' : 'empty',
            'slot4' : 'empty',
            'slot5' : 'empty',
            'slot6' : 'empty',
            'slot7' : 'empty',
            'slot8' : 'empty',
            'slot9' : 'empty',
            'slot10' : 'empty',
            'slot11' : 'empty',
            'slot12' : 'empty',
            'slot13' : 'empty',
            'slot14' : 'empty',
            'slot15' : 'empty',
            'slot16' : 'empty',
            'slot17' : 'empty',
            'slot18' : 'empty',
            'slot19' : 'empty',
            'slot20' : 'empty',
            'slot21' : 'empty',
            'slot22' : 'empty',
            'slot23' : 'empty',
            'slot24' : 'empty',
            'slot25' : 'empty',
            'slot26' : 'empty',
            'slot27' : 'empty',
            'slot28' : 'empty',
            'slot29' : 'empty',
            'slot30' : 'empty'},
        'pets' : {'1' : 'none',
            '2' : 'none',
            '3' : 'none',
            '4' : 'none',
            '5' : 'none'},
        'ratks' : {'1' : 'punch', #r atks are regular
            '2' : 'kick',
            '3' : 'jab',  #'s 1-3 are lvl 1 atks
            '4' : 'locked', #lvl 5 atk unlock
            '5' : 'locked', #lvl 10 atk unlock (roundhouse kick)
            '6' : 'locked'}, #lvl 50 atk unlock (elemental ball)
        'aatks' : {'1' : 'locked',#a atks are assistant; #1 is lvl 10 unlock
            '2' : 'locked', #2 is lvl 30 unlock
            '3' : 'locked', #3 is level 50 unlock
            '4' : 'locked'}, #4 is secret unlock
        'satks' : {'1' : 'locked',   #s atks are special; #1 is lvl 25 unlock
            '2' : 'locked', #2 is secret unlock
            '3' : 'locked'},#3 is boneandblood trophy
        'matks' : {'1' : 'locked'}}  #m atks are mega, #1 is lvl 100 unlock
hero = player

altPlayer = {'lvl' : 1, #level
        'name' : 'bob',
        'xp' : 0, # experience
        'lvlNext' : 50, #xp goal to next lvl
        'stage' : 0,
        'stats' : {'str' : 1.5, #strength
            'dex' : 1.5, #dexterity or skill
            'int' : 1.5, #intelligence
            'hp' : 15, #current health
            'maxHp': 15, #maximum health
            'speed' : 1.5,
            'luck' : 0.5,
            'crowns' : 10,
            'doubloons' : 0,
            'jewels' : 0,
            'atk' : [2, 12]},
        'gear' : {'helmet' : 'empty',
                  'chestpiece' : 'empty',
                  'leggings' : 'empty',
                  'boots' : 'empty',
                  'rings' : {'1' : 'Ring of Runes',
                             '2' : 'empty',
                             '3' : 'empty'},
                  'equippedrings' : {'leftpinky' : 'Ring of Runes',
                                     'rightpinky' : 'empty'}},
        'items' : {'primary' : 'empty',
            'secondary' : 'empty',
            'melee' : 'empty',
            'slot1' : 'empty',
            'slot2' : 'empty',
            'slot3' : 'empty',
            'potion1' : 'empty',
            'potion2' : 'empty'},
        'ratks' : {'1' : 'punch', #regular attacks, available during any battle
            '2' : 'kick',
            '3' : 'jab'},
        'batks' : {'1' : 'glorious stance'}} #boss attacks, only usable during bosses

modernPlayer = {'lvl' : 1, #level
        'xp' : 0, # experience
        'name' : 'bob',
        'lvlNext' : 25, #xp goal to next lvl
        'location' : '',
        'role' : 'unaffiliated',
        'stats' : {'str' : 1, #strength
            'dex' : 1, #dexterity or skill
            'int' : 1, #intelligence
            'hacking' : 0, #hacking capacity
            'medical' : 0, #medical skills
            'cybergadgets' : 0, #cyber-gadgets
            'serums' : 0, #serum-making skill
            'hp' : 30, #current health
            'maxHp': 30, #maximum health
            'speed' : 1,
            'luck' : 1,
            'crowns' : 10,
            'doubloons' : 0,
            'jewels' : 0,
            'atk' : [2, 12]},
        'items' : {'slot1' : 'empty',
            'slot2' : 'empty',
            'slot3' : 'empty',
            'slot4' : 'empty',
            'slot5' : 'empty',
            'slot6' : 'empty',
            'slot7' : 'empty',
            'slot8' : 'empty',
            'slot9' : 'empty',
            'slot10' : 'empty',
            'slot11' : 'empty',
            'slot12' : 'empty',
            'slot13' : 'empty',
            'slot14' : 'empty',
            'slot15' : 'empty',
            'slot16' : 'empty',
            'slot17' : 'empty',
            'slot18' : 'empty',
            'slot19' : 'empty',
            'slot20' : 'empty',
            'slot21' : 'empty',
            'slot22' : 'empty',
            'slot23' : 'empty',
            'slot24' : 'empty',
            'slot25' : 'empty',
            'slot26' : 'empty',
            'slot27' : 'empty',
            'slot28' : 'empty',
            'slot29' : 'empty',
            'slot30' : 'empty'},
        'pets' : {'1' : 'none',
            '2' : 'none',
            '3' : 'none',
            '4' : 'none',
            '5' : 'none'},
        'ratks' : {'1' : 'punch', #r atks are regular
            '2' : 'kick',
            '3' : 'jab',  #'s 1-3 are lvl 1 atks
            '4' : 'locked', #lvl 5 atk unlock
            '5' : 'locked', #lvl 10 atk unlock (roundhouse kick)
            '6' : 'locked'}, #lvl 50 atk unlock (elemental ball)
        'aatks' : {'1' : 'locked',#a atks are assistant; #1 is lvl 10 unlock
            '2' : 'locked', #2 is lvl 30 unlock
            '3' : 'locked', #3 is level 50 unlock
            '4' : 'locked'}, #4 is secret unlock
        'satks' : {'1' : 'locked',   #s atks are special; #1 is lvl 25 unlock
            '2' : 'locked', #2 is secret unlock
            '3' : 'locked'},#3 is boneandblood trophy
        'matks' : {'1' : 'locked'}}  #m atks are mega, #1 is lvl 100 unlock
mHero = modernPlayer

def playerTakeDmg(attacker, defender):
    dmg = random.randint(attacker['stats']['atk'][0], \
                         attacker['stats']['atk'][1])
    defender['stats']['hp'] -= dmg
    if defender['stats']['hp'] <= 0:
        sprint(f'{defender["name"]} has been slain.\n')
        if defender == hero:
            sprint('You died!\n')
            sprint('Would you like to continue? Y/')
            gameover = input('N ').lower()
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
        if defender == hero:
            sprint('You died!\n')
            sprint('Would you like to continue? Y/')
            gameover = input('N ').lower()
            if gameover == 'y':
                load()
            elif gameover == 'n':
                sprint('Game Over!\n')
                time.sleep(5)
                sys.exit()
    sprint(f'{defender["name"]} takes {dmg} damage!\n')
    commands(defender, attacker)

def enemyTakeDmg(attacker, defender):
    atks = (sorted(attacker['ratks']) + sorted(attacker['aatks']) + sorted(attacker['satks']) + sorted(attacker['matks']))
    sprint(atks)
    sprint('Choose your attack')
    dmg = input(': ')
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
        if defender == hero:
            sprint('You died!\n')
            sprint('Would you like to continue? Y/')
            gameover = input('N ').lower()
            if gameover == 'y':
                load()
            if gameover == 'n':
                sprint('Game Over!\n')
                time.sleep(5)
                sys.exit()
        if attacker == hero:
            if defender == ghost:
                if attacker['pets']['slot1'] == 'empty':
                        attacker['pets']['slot1'] = defender['reward']
                        sprint(f'You\'ve obtained {defender["reward"]}!\n')
                if attacker['pets']['slot1'] != 'empty':
                    for slots in attacker['pets']:
                        if slot in slots == 'empty':
                            slot = defender['reward']
                    sprint(f'You\'ve obtained {defender["reward"]}!\n')
                    attacker['xp'] += defender['xpreward']
                    level(attacker)
            if defender == dragon:
                    if attacker['items']['slot1'] == 'empty':
                        random.shuffle(dragon['reward'])
                        attacker['items']['slot1'] = defender['reward'][0]
                        sprint(f'You\'ve obtained {defender["reward"[0]]}!\n')
                    if attacker['items']['slot1'] != 'empty':
                        for slots in attacker['items']:
                            if slot in slots == 'empty':
                                slot = defender['reward']
                        sprint(f'You\'ve obtained {defender["reward"]}!\n')
                        attacker['xp'] += defender['xpreward']
                        level(attacker)
            if attacker['items']['slot1'] == 'empty':
                attacker['items']['slot1'] = defender['reward']
                sprint(f'You\'ve obtained {defender["reward"]}!\n')
            for slots in attacker['items']:
                if slot in slots == 'empty':
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
                pass
            if choose == 'heal':
                player['stats']['str'] -= 5
                player['stats']['hp'] += 10
                if player['stats']['hp'] > player['stats']['maxHp']:
                    player['stats']['hp'] = player['stats']['maxHp']
                pass
            if choose == 'money':
                player['stats']['str'] -= 5
                player['stats']['dex'] -= 5
                amount = random.randint[(5*(player['lvl'])), (10*(player['lvl']))]
                currencies=['jewels', 'crowns', 'doubloons']
                random.shuffle(currencies)
                x=currencies[0]
                player['stats'][x] += amount
                pass
        if cast == 'no':
            pass
    if knowledge  >= 10:
        sprint('Would you like to cast a heal or power spell')
        cast = input("? ").lower()
        if cast == 'yes':
            sprint('Power or Heal')
            choose = input('? ').lower()
            if choose == 'power':
                player["stats"]['str'] += 5
                player['stats']['atk'][1] += 3
                player['stats']['hp'] -= 10
                pass
            if choose == 'heal':
                player['stats']['str'] -= 1
                player['stats']['hp'] += 1
                if player['stats']['hp'] > player['stats']['maxHp']:
                    player['stats']['hp'] = player['stats']['maxHp']
                pass
        if cast == 'no':
            pass
    if knowledge >= 5:
        sprint('Would you like to cast a basic heal spell')
        cast = input("? ").lower()
        if cast == 'no':
            pass
        if cast == 'yes':
            player['stats']['str'] -= 1
            player['stats']['hp'] += 1
            if player['stats']['hp'] > player['stats']['maxHp']:
                player['stats']['hp'] = player['stats']['maxHp']
            pass
    sprint(player['stats'])

b=0
c=0
DevMode=0
thirteenKnightMode=0
ModernMode=0

def start():
    global a
    a:int = 0
    if DevMode==0 and thirteenKnightMode==1:
        sprint('-----The Thirteenth Knight-----\n1) New Game\n2) Settings\n3) Bonus Content\n-------------------------------\n')
        Selection = input('> ')
        try:
            a=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            start()
    elif DevMode==1 and thirteenKnightMode==0:
        sprint('-----The Twelfth Knight-----\n1) New Game\n2) Load Game\n3) Settings\n4) Bonus Content\n5) DEVTOOLS\n----------------------------\n')
        Selection = input('> ')
        try:
            a=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            start()
    else:
        sprint('-----The Twelfth Knight-----\n1) New Game\n2) Load Game\n3) Settings\n4) Bonus Content\n----------------------------\n')
        Selection = input('> ')
        try:
            a=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            start()

def UNDEV():
        sprint('ARE YOU SURE YOU WANT TO EXIT DEVELOPER MODE? Y/')
        undev=input('N ').lower()
        if undev=='y':
            sprint('THANK YOU FOR USING DEVELOPER MODE.\n')
            time.sleep(.2)
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            DevMode=0
            start()
        elif undev=='n':
            sprint('DEVELOPER MODE WILL STAY ACTIVE.\n')

while c==0:
    c=1
    if 'idlelib.run' not in sys.modules:
        os.system('cls' if os.name == 'nt' else 'clear')
    start()

while b==0:
    if a==1 and thirteenKnightMode==0 and ModernMode==0:
        b=1
        a=0
        sprint('Enter the chosen one\'s name')
        name=input(': ')
        hero['name'] = name
        sprint('Choose your primary talent: |Mage|Healer|Soldier|Scientist')
        role=input('| ').lower()
        hero['role'] = role
        if role=='mage':
            sprint('You have become a mage!\nYou magical abilities are growing!\nAs the magic flows \
through you, you get more powerful!\nMagic increased to 5!\n')
            hero['stats']['mag'] = 5
        elif role=='healer':
            sprint('You have become a healer!\nYou medical abilities are growing!\nAs you help more \
people, you get more skills!\nHealth increased to 35!\n')
            hero['stats']['hp'] = 35
            hero['stats']['maxHp'] = 35
        elif role=='soldier':
            sprint('You have become a soldier!\nYou attacking capabilities are growing!\nAs your sword slashes \
through your oppenents, you get more skilled!\nSpeed, Strength, and Dexterity increased to 5!\n')
            hero['stats']['str'] = 5
            hero['stats']['dex'] = 5
            hero['stats']['speed'] = 5
        elif role=='scientist':
            sprint('You have become a scientist!\nYou chemical abilities are growing!\nAs the knowledge floods \
your mind, you get smarter!\nIntelligence increased to 5!\n')
            hero['stats']['int'] = 5
        else:
            b=0
            a=1
    elif a==1 and thirteenKnightMode==0 and ModernMode==1:
        b=1
        a=0
        sprint('Enter the chosen one\'s name')
        name=input(': ')
        hero['name'] = name
        sprint('Choose your primary talent: |Medic|Cybersoldier|Scientist|Hacker')
        role=input('| ').lower()
        hero['role'] = role
        if role=='hacker':
            sprint('You have become a hacker!\nYou can hack advanced electronics!\nHacking abilities increased from minimal to veteran!\n')
            modernPlayer['stats']['hacking'] = 1
        elif role=='medic':
            sprint('You have become a medic!\nYou medical abilities are growing!\nAs you help more \
people, you get more skills!\nYou can now do advanced medical procedures!\n')
            modernPlayer['stats']['medical'] = 1
        elif role=='cybersoldier':
            sprint('You have become a cybersoldier!\nYou attacking capabilities are growing!\nAs your digital implant enhances \
your body, you get more agile and tactical!\nYou can now use advanced military grade cybertechnology without hacking or alarms!\n')
            modernPlayer['stats']['cybergadgets'] = 1
        elif role=='scientist':
            sprint('You have become a scientist!\nYou chemical abilities are growing!\nAs the knowledge floods \
your mind, you get smarter!\nYou can now make serums!\n')
            modernPlayer['stats']['serums'] = 1
        else:
            b=0
            a=1
    elif a==1 and thirteenKnightMode==1:
        b=1
        a=0
        sprint('Enter the chosen one\'s name')
        name=input(': ')
        hero['name'] = name
        sprint('Choose your role: |No roles availible|\n')
        sprint('13 Knight Mode is a short, EXTREME, tournament of battles.\nAre you sure you want to proceed? Y/')
        t=input('N ').lower()
        if t=='n':
            sprint('13 Knight Mode will be deactivated.\nYou can reactivate it buy entering the code again.\n')
            thirteenKnightMode=0
            b=0
            start()
        elif t=='y':
            sprint('YOU CANNOT SAVE. There are 50 levels in all.\nAre you really sure you want to proceed? Y/')
            confirm=input('N ').lower()
            if confirm=='y':
                with open("AlternateTournament.py") as file:
                    exec(file.read())
            if confirm=='n':
                sprint('13 Knight Mode will be deactivated.\nYou can reactivate it buy entering the code again.\n')
                thirteenKnightMode=0
                b=0
                start()
    elif a==2 and thirteenKnightMode==0:
        try:
            b=1
            a=0
            load()
        except FileNotFoundError:
            a=0
            b=0
            sprint('> No Save file found\n')
            time.sleep(.2)
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            start()
    elif (a==3 and thirteenKnightMode==0) or (a==2 and thirteenKnightMode==1):
        a=0
        b=1
        sprint('Choose what setting to change: |Back|Dialogue Speed|Difficulty')
        settingedit=input('| ').lower()
        if settingedit=='dialogue speed':
            sprint('What speed should dialogue be spoken?\nSlowest is 1, Fastest is 3')
            sps=input('. ')
            try:
                if int(sps)>=3:
                    def sprint(str):              #Faster Typing
                        for letter in str:
                            sys.stdout.write(letter)
                            sys.stdout.flush()
                            time.sleep(.01)
                elif int(sps)<=1:
                    def sprint(str):              #Slower Typing
                        for letter in str:
                            sys.stdout.write(letter)
                            sys.stdout.flush()
                            time.sleep(.1)
                elif int(sps)==2:
                    def sprint(str):
                        for letter in str:
                            sys.stdout.write(letter)
                            sys.stdout.flush()
                            time.sleep(.04)
                b=0
                time.sleep(.5)
                start()
            except ValueError:
                a=3
                b=0
                sprint('Err: UnknownSpeedValue. Attempt again.\n')
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
        elif settingedit=='difficulty' and thirteenKnightMode==0:
            sprint('What should be set? 1-')
            diff=input('3 ')
            try:
                if diff=='1':
                    hero['maxHp']=50
                    hero['hp']=hero['maxHp']
                    hero['atk']=[5, 15]
                    sprint('Hp has been set to 50/50,\nAtk range has been set from 5 to 15..\n')
                elif diff=='2':
                    hero['maxHp']=30
                    hero['hp']=hero['maxHp']
                    hero['atk']=[2, 12]
                    sprint('Hp has been set to 30/30,\nAtk range has been set from 2 to 12.\n')
                elif diff=='3':
                    hero['maxHp']=10
                    hero['hp']=hero['maxHp']
                    hero['atk']=[0, 9]
                    sprint('Hp has been set to 10/10,\nAtk range has been set from 0 to 9.\n')
                b=0
                time.sleep(.5)
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                start()
            except ValueError:
                a=3
                b=0
                sprint('Err: UnknownDifficultySetting. Attempt again.\n')
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
        elif settingedit=='back':
            a=0
            b=0
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            start()
        else:
            a=3
            b=0
            sprint('Err: UnknownOption. Attempt again.\n')
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
    elif (a==4 and thirteenKnightMode==0) or (a==3 and thirteenKnightMode==1):
        sprint('|Buy DLC|Enter Code|Disable Codes')
        bonus=input('| ').lower()
        if bonus=='buy dlc':
            b=1
            a=0
            sprint('DLC List:\n-Legend Armor-   -7500-\n-Resurrection Spell Recipe-   -5000-\n\n')
            sprint('Enter wanted DLC')
            content=input(': ').lower()
            sprint('\nCost: ' + dlcCost[content] + '\n')
            sprint('Are you sure you want purchase this? Y\\N')
            confirm = input(' ').lower()
            if confirm == 'n':
                sprint('\nCancelling purchase...\n')
                time.sleep(2)
            elif confirm == 'y':
                sprint('Charging account...\n')
                time.sleep(1)
                if megaGems < dlcCost[content]:
                    sprint('Not enough Mega Gems.\nWould you like to buy more? Y\\')
                    buy = input('N ').lower()
                    if buy == 'n':
                        sprint('Returning to Title Screen.\n')
                    elif buy == 'y':
                        sprint('How many would you like to buy?\n-50\n-100\n-500\n-1000\n-5000\n-10000\n')
                        spend = input('')

                elif megaGems >= dlcCost[content]:
                    megaGems -= dlcCost[content]
                    sprint(megaGems + ' Mega Gems left.')
            b=0
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            start()
        elif bonus == 'enter code':
            a = 0
            b = 1
            sprint('Enter code')
            diff = input(': ')
            if diff == 'DevMode':
                if thirteenKnightMode == 0:
                    sprint('CODE INSERTED SUCCESSFULLY. \"DEVELOPER TOOLS\" ADDED TO TITLE SCREEN.\n')
                    time.sleep(.8)
                    sprint('YOU CAN ENTER "UNDEV()" INTO THE DEVELOPER TERMINAL TO EXIT DEVMODE.\n')
                    DevMode=1
                    b=0
                    time.sleep(2.5)
                    if 'idlelib.run' in sys.modules:
                        sprint('\n############################\n\n')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    start()
                elif thirteenKnightMode == 1:
                    sprint('CODE INTERFERED WITH ANOTHER CODE.\nWOULD YOU LIKE TO DISABLE THE OTHER CODE? Y/')
                    i=input('N ').lower()
                    if i == 'n':
                        sprint('CODE NOT INSERTED.\nDISABLE INTERFERING CODE TO ENABLE DEVELOPER MODE.\n')
                        b=0
                        start()
                    elif i == 'y':
                        sprint('DISABLING INTERFERING CODE...')
                        time.sleep(.5)
                        sprint('INSERTING NEW CODE.\nCODE INSERTED SUCCESSFULLY. \"DEVELOPER TOOLS\" ADDED TO TITLE SCREEN.\n')
                        time.sleep(.8)
                        sprint('YOU CAN ENTER "UNDEV()" INTO THE DEVELOPER TERMINAL TO EXIT DEVMODE.\n')
                        DevMode=1
                        thirteenKnightMode=0
                        b=0
                        time.sleep(5)
                        if 'idlelib.run' in sys.modules:
                            sprint('\n############################\n\n')
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        start()
            elif diff == 'ThirteenthKnight':
                if DevMode==0:
                    sprint('CODE INSERTED SUCCESSFULLY. \"THIRTEENTH KNIGHT MODE\" UNLOCKED.\n')
                    thirteenKnightMode=1
                    b=0
                    time.sleep(2.5)
                    if 'idlelib.run' in sys.modules:
                        sprint('\n############################\n\n')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    start()
                elif DevMode==1:
                    sprint('CODE INTERFERED WITH ANOTHER CODE.\nWOULD YOU LIKE TO DISABLE THE OTHER CODE? Y/')
                    i=input('N ').lower()
                    if i=='n':
                        sprint('CODE NOT INSERTED.\nDISABLE INTERFERING CODE TO ENABLE THIRTEEN KNIGHT MODE.\n')
                        b=0
                        start()
                    elif i=='y':
                        sprint('DISABLING INTERFERING CODE...\n')
                        time.sleep(1.2)
                        sprint('INSERTING NEW CODE.\nCODE INSERTED SUCCESSFULLY. \"THIRTEENTH KNIGHT MODE\" ADDED TO TITLE SCREEN.\n')
                        time.sleep(.8)
                        thirteenKnightMode=1
                        DevMode=0
                        b=0
                        time.sleep(5)
                        if 'idlelib.run' in sys.modules:
                            sprint('\n############################\n\n')
                        else:
                            os.system('cls' if os.name == 'nt' else 'clear')
                        start()
            elif diff=='ModernMode':
                sprint('CODE INSERTED SUCCESSFULLY. A modernized version has appeared when starting a new game\n')
                ModernMode=1
                b=0
                time.sleep(3)
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                start()
            else:
                sprint('CODE REJECTED. INSERT VALID CODE.\n')
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                if thirteenKnightMode==0:
                    a=4
                elif thirteenKnightMode==1:
                    a=3
                b=0
        elif bonus=='disable codes':
            b=1
            a=0
            if ModernMode==0 and DevMode==0 and thirteenKnightMode==0:
                sprint('NO CODES TO DISABLE. HAVE A NICE DAY.\n')
                b=0
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                start()
            elif ModernMode==1 or DevMode==1 or thirteenKnightMode==1:
                sprint('DISABLING ALL CODES...\n')
                time.sleep(1.2)
                ModernMode=0
                DevMode=0
                thirteenKnightMode=0
                b=0
                if 'idlelib.run' in sys.modules:
                    sprint('\n############################\n\n')
                else:
                    os.system('cls' if os.name == 'nt' else 'clear')
                start()
        else:
            b=0
            a=4
            sprint('Err: UnknownOption. Re-Attempt.\n')
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
    elif a==5 and DevMode==1 and thirteenKnightMode==0:
        b=1
        a=0
        sprint('WELCOME TO DEVMODE! AVAILABLE TOOLS ARE:\n')
        time.sleep(.3)
        sprint('-TERMINAL\n')
        time.sleep(.4)
        sprint('-DEBUG\n')
        time.sleep(.4)
        sprint('-HELP\n')
        time.sleep(.4)
        sprint('-MORE TOOLS COMING SOON!-\n')
        t=input('~ ').lower()
        if t=='terminal':
            sys.exit()
        elif t=='debug':
            import pdb; pdb.set_trace()
        elif t=='help':
            sprint('DEVELOPER MODE HELP TOOL\n    TERMINAL-\n        THE STANDARD PROMPT WHEN USING THE PYTHON SHELL.\
\n\n    DEBUG-\n        A DEBUG MODE USING THE PDB MODULE. EXITS INTO THE TERMINAL.\n        NOT RECOMMENDED FOR AMATEURS.\n')
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            a=5
            b=0
        else:
            sprint('ERR: UNKNOWNOPTION. ATTEMPT AGAIN.\n')
            if 'idlelib.run' in sys.modules:
                sprint('\n############################\n\n')
            else:
                os.system('cls' if os.name == 'nt' else 'clear')
            a=5
            b=0
    else:
        b=0
        a=0
        sprint('Invalid Value. Choose a listed option please.\n')
        start()
