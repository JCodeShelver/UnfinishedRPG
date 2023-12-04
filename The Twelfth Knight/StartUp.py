import os
import pickle
import random
import sys
import time
dlcCost = {'legend armor' : 7500,
           'resurrection spell recipe' : 5000}
def sprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)

def clear():
    if 'idlelib.run' in sys.modules:
        sprint('\n############################\n\n')
    else:
        os.system('cls' if os.name == 'nt' else 'clear')

if 'idlelib.run' in sys.modules:
    pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')

#--------ITEM IDS--------#
#tier 1 > common
#tier 2 > uncommon
#tier 3 > rare
#tier 4 > epic
#tier 5 > legendary
#tier 6 > mystical
#tier 7 > radiant
#tier 8 > stellar
#tier 9 > astral
itemBook = {
    'item1' : {'legend armor' : 'mystical',
           'obtained' : 'dlc',
           'cost' : '7500'},
    'item2' : {'resurrection spell recipe' : 'mystical',
           'obtained' : 'dlc',
           'cost' : '5000'},
    'item3' : {'gold cannon' : 'rare',
           'obtained' : 'sailor',
           'cost' : '9500'}
    #item4={},
    #item5={},
    #item6={},
    #item7={},
    #item8={},
    }

#-----------------------------------Map Layout-----------------------------------
zone0 = {
    'c3': {
        'name':'Portal Hub',
        'description':'A collection of portals to take you to almost anywhere.',
        'examination':'examine',
        'solved':False,
        'up':'c2',
        'down':'c4',
        'left':'b3',
        'right':'d3'},
    'c2': {
        'name':'Boss Portals',
        'description':'Portals that lead to bosses.',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'c3',
        'left':'',
        'right':''},
    'c4': {
        'name':'Transdimensional Portals',
        'description':'Portals that lead to other dimensions.',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'',
        'left':'c3',
        'right':''},
    'b3': {
        'name':'The Grand Portals',
        'description':'Portals that are lead to different times.',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'',
        'left':'',
        'right':'c3'},
    'd3': {
        'name':'The Nameless Gateway',
        'description':'A portal that leads to the core of this realm.',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'',
        'left':'c3',
        'right':''}}
zone1 = {
    'a1': {
        'name':'Home',
        'description':'This is the home you live in.',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'a2',
        'left':'',
        'right':'b1'},
    'a2': {
        'name':'Town Outskirts',
        'description':'The outer parts of the town.',
        'examination':'examine',
        'solved':False,
        'up':'a1',
        'down':'a3',
        'left':'',
        'right':'b2'},
    'a3': {
        'name':'Town Plaza',
        'description':'This is the majority of the city.',
        'examination':'examine',
        'solved':False,
        'up':'a2',
        'down':'a4',
        'left':'',
        'right':'b3'},
    'a4': {
        'name':'Town Market',
        'description':'This is the market, the local shops.',
        'examination':'examine',
        'solved':False,
        'up':'a3',
        'down':'a5',
        'left':'',
        'right':'b4'},
    'a5': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'a4',
        'down':'',
        'left':'',
        'right':'b5'},
    'b1': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'b2',
        'left':'a1',
        'right':'c1'},
    'b2': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'b1',
        'down':'b3',
        'left':'a2',
        'right':'c2'},
    'b3': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'b2',
        'down':'b4',
        'left':'a3',
        'right':'c3'},
    'b4': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'b3',
        'down':'b5',
        'left':'a4',
        'right':'c4'},
    'b5': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'b4',
        'down':'',
        'left':'a5',
        'right':'c5'},
    'c1': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'c2',
        'left':'b1',
        'right':'d1'},
    'c2': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'c1',
        'down':'c3',
        'left':'b2',
        'right':'d2'},
    'c3': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'c2',
        'down':'c4',
        'left':'b3',
        'right':'d3'},
    'c4': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'c3',
        'down':'c5',
        'left':'b4',
        'right':'d4'},
    'c5': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'c4',
        'down':'',
        'left':'b5',
        'right':'d5'},
    'd1': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'d2',
        'left':'c1',
        'right':'e1'},
    'd2': {
        'name':'Portal Shrine',
        'description':'A shrine that looks like it\'s for a portal.\nUnfortunately for you, it is inoperable.',
        'examination':'You notice there are runes on the seven cylindrical pillars, with odd indents on the top of each.',
        'solved':False,
        'up':'d1',
        'down':'d3',
        'left':'c2',
        'right':'e2'},
    'd3': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'d2',
        'down':'d4',
        'left':'c3',
        'right':'e3'},
    'd4': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'d3',
        'down':'d5',
        'left':'c4',
        'right':'e4'},
    'd5': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'d4',
        'down':'',
        'left':'c5',
        'right':'e5'},
    'e1': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'',
        'down':'e2',
        'left':'d1',
        'right':''},
    'e2': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'e1',
        'down':'e3',
        'left':'d2',
        'right':''},
    'e3': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'e2',
        'down':'e4',
        'left':'d3',
        'right':''},
    'e4': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'e3',
        'down':'e5',
        'left':'d4',
        'right':''},
    'e5': {
        'name':'',
        'description':'',
        'examination':'examine',
        'solved':False,
        'up':'e4',
        'down':'',
        'left':'d5',
        'right':''}}

oldLocation=zone1['a1']
#-------Chests-------#
portalKeyChest = {'abbrLocation' : 'z4b4',
                'contents' : {'slot1':'Portal Shrine Key',
                              'slot2':'Transdimensional Portal Gate Key'}}

#-------Default Player (gets overrided if user loads a game)-------#
player = {'lvl' : 1, #level
        'xp' : 0, # experience
        'name' : 'bob',
        'gameOver' : 0,
        'lvlNext' : 25, #xp goal to next lvl
        'oldLocation' : oldLocation,
        'abbrLocation' : 'z1a1',
        'location' : zone1['a1'],
        'savefile' : 0,
        'role' : 'unaffiliated',
        'portals' : 0,
        'stats' : {'str' : 1, #strength
            'dex' : 1, #dexterity or skill
            'int' : 1, #intelligence
            'mag' : 1, #magic
            'hp' : 30, #current health
            'maxHp' : 30, #maximum health
            'lives' : 3, #lives left
            'speed' : 1,
            'luck' : 1,
            'megaGems' : 50,
            'crowns' : 10,
            'doubloons' : 0,
            'jewels' : 0,
            'atk' : [2, 12]},
        'gear' : {'helmet' : ['empty'],
                  'chestpiece' : ['empty'],
                  'leggings' : ['empty'],
                  'boots' : ['empty'],
                  'rings' : {'1' : 'Ring of Runes',
                             '2' : 'empty',
                             '3' : 'empty'},
                  'equippedrings' : {'leftpinky' : 'Ring of Runes',
                                     'rightpinky' : 'empty'}},
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

def prompt():
    sprint('\n===========================\n')
    sprint('What would you like to do?\n')
    action = input('> ')
    acceptable_actions = ['move', 'go', 'travel', 'walk', 'quit', 'exit', 'examine', 'inspect', 'interact', 'look', 'save']
    while action.lower() not in acceptable_actions:
        sprint('Enter a valid action please.\n')
        action = input('> ')
    if action.lower() in ['move', 'go', 'travel', 'walk']:
        move()
    elif action.lower() in ['quit', 'exit', 'stop']:
        if player['location'] != zone0["c3"]:
            sprint('Would you like to save? Y/N')
            sav = input(' ').lower()
            if sav=='y':
                save()
                time.sleep(1)
                sys.exit()
            elif sav=='n':
                sys.exit()
            else:
                save()
                time.sleep(1)
                sys.exit()
        elif player['location'] == zone0["c3"]:
            sprint('Would you like to exit the Portal Realm? Y/N')
            goBack = input(' ').lower()
            if goBack == 'y':
                player['oldLocation'] = player['location']
                time.sleep(1)
                sprint('You left the Portal Realm, located at the Portal Shrine as if\
if no time passed. Odd...')
            elif goBack =='n':
                prompt()
            else:
                save()
                time.sleep(1)
                sys.exit()
    elif action.lower() in ['examine', 'inspect', 'interact', 'look']:
        examine()
    elif action.lower() == 'save':
        save()
    prompt()

def move():
    sprint('Which direction would you like to move in')
    dest = input('? ')
    directions = ['up', 'north', 'down', 'south', 'left', 'west', 'right', 'east']
    if dest=='north':
        dest='up'
    elif dest=='south':
        dest='down'
    elif dest=='west':
        dest='left'
    elif dest=='east':
        dest='right'
    while dest not in directions or player['location'][dest] == '':
        sprint('Unknown direction or cannot move that direction.\n')
        sprint('Which direction would you like to move in')
        dest = input('? ')
        if dest=='north':
            dest='up'
        elif dest=='south':
            dest='down'
        elif dest=='west':
            dest='left'
        elif dest=='east':
            dest='right'
    if dest=='up':
        player['location'] = player['location']['up']
    elif dest=='down':
        player['location'] = player['location']['down']
    elif dest=='left':
        player['location'] = player['location']['left']
    elif dest=='right':
        player['location'] = player['location']['right']
    player['oldLocation'] = player['location']

def examine():
    if player['location']['solved']==True:
        sprint('There\'s nothing to do here.\n')
    else:
        print(player['location']['examination'])

def atkUnlocks(pLvl):               #enter 'player['lvl'] or hero['lvl']
    if pLvl >= 100:
        if player['matks']['1'] != 'supernova':
            player['matks']['1'] = 'supernova'
            sprint ('You unlocked your first mega attack, supernova!\n')
        if player['ratks']['4'] != 'theknee':
            player['ratks']['4'] = 'theknee'
            sprint ('You unlocked the knee attack!\n')
        if player['ratks']['5'] != 'roundhousekick' and player['aatks']['1'] != 'bullrage':
            player['ratks']['5'] = 'roundhousekick'
            player['aatks']['1'] = 'bullrage'
            sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        if player['satks']['1'] != 'swordslicers':
            player['satks']['1'] = 'swordslicers'
            sprint ('You unlocked your first special attack, sword slicers!\n')
        if player['aatks']['2'] != 'sciencegleam':
            player['aatks']['2'] = 'sciencegleam'
            sprint ('You unlocked science gleam!\n')
        if player['ratks']['6'] != 'elementalball' and player['aatks']['3'] != 'swordoflight':
            player['ratks']['6'] = 'elementalball'
            player['aatks']['3'] = 'swordoflight'
            sprint ('You unlocked the elemental ball, and the sword of light!\n')
    elif pLvl >= 50:
        if player['ratks']['4'] != 'theknee':
            player['ratks']['4'] = 'theknee'
            sprint ('You unlocked the knee attack!\n')
        if player['ratks']['5'] != 'roundhousekick' and player['aatks']['1'] != 'bullrage':
            player['ratks']['5'] = 'roundhousekick'
            player['aatks']['1'] = 'bullrage'
            sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        if player['satks']['1'] != 'swordslicers':
            player['satks']['1'] = 'swordslicers'
            sprint ('You unlocked your first special attack, sword slicers!\n')
        if player['aatks']['2'] != 'sciencegleam':
            player['aatks']['2'] = 'sciencegleam'
            sprint ('You unlocked science gleam!\n')
        if player['ratks']['6'] != 'elementalball' and player['aatks']['3'] != 'swordoflight':
            player['ratks']['6'] = 'elementalball'
            player['aatks']['3'] = 'swordoflight'
            sprint ('You unlocked the elemental ball, and the sword of light!\n')
    elif pLvl >= 30:
        if player['ratks']['4'] != 'theknee':
            player['ratks']['4'] = 'theknee'
            sprint ('You unlocked the knee attack!\n')
        if player['ratks']['5'] != 'roundhousekick' and player['aatks']['1'] != 'bullrage':
            player['ratks']['5'] = 'roundhousekick'
            player['aatks']['1'] = 'bullrage'
            sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        if player['satks']['1'] != 'swordslicers':
            player['satks']['1'] = 'swordslicers'
            sprint ('You unlocked your first special attack, sword slicers!\n')
        if player['aatks']['2'] != 'sciencegleam':
            player['aatks']['2'] = 'sciencegleam'
            sprint ('You unlocked science gleam!\n')
    elif pLvl >= 25:
        if player['ratks']['4'] != 'theknee':
            player['ratks']['4'] = 'theknee'
            sprint ('You unlocked the knee attack!\n')
        if player['ratks']['5'] != 'roundhousekick' and player['aatks']['1'] != 'bullrage':
            player['ratks']['5'] = 'roundhousekick'
            player['aatks']['1'] = 'bullrage'
            sprint ('You unlocked the round house kick attack, and your first assistant attack, bullrage!\n')
        if player['satks']['1'] != 'swordslicers':
            player['satks']['1'] = 'swordslicers'
            sprint ('You unlocked your first special attack, sword slicers!\n')
    elif pLvl >= 10:
        if player['ratks']['4'] != 'theknee':
            player['ratks']['4'] = 'theknee'
            sprint ('You unlocked the knee attack!\n')
        if player['ratks']['5'] != 'roundhousekick' and player['aatks']['1'] != 'bullrage':
            player['ratks']['5'] = 'roundhousekick'
            player['aatks']['1'] = 'bullrage'
    elif pLvl >= 5:
        if player['ratks']['4'] != 'theknee':
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
            nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, 0
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
                sprint('You have reached the max level! Congratulations, {}!\n'.format(pStats['name']))
            sprint('Level:', pStats['lvl'])
            sprint('Exp:', pStats['xp'])
            sprint('Stats: STRENGTH {} +{}, DEXTERITY {} +{}, INTELLIGENCE {} +{}, HEALTH {} +{}, ATTACK {}, {} +{}, {}, MAGIC {} +{}\n'.format(pStats['stats']['str'], nStr,
                                                                                                                       pStats['stats']['dex'], nDex,
                                                                                                                       pStats['stats']['int'], nInt,
                                                                                                                       pStats['stats']['hp'], nHp,
                                                                                                                       pStats['stats']['atk'][0], pStats['stats']['atk'][1],
                                                                                                                       nAtkDmg[0], nAtkDmg[1], pStats['stats']['mag'], nMag))
            pStats['stats']['atk'][0] += nAtkDmg[0]
            pStats['stats']['atk'][1] += nAtkDmg[1]
            pStats['stats']['hp'] += nHp
            pStats['stats']['maxHp'] += nMaxHp
            pStats['stats']['str'] += nStr
            pStats['stats']['dex'] += nDex
            pStats['stats']['int'] += nInt
            pStats['stats']['mag'] += nMag
            sprint('Exp left required to gain a level:\n ', pStats['lvlNext'] - pStats['xp'])
            sprint('Exp required total to gain level:\n ', pStats['lvlNext'])
            nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, 0
            sprint('------------------------------\n')
            atkUnlocks(pStats['lvl'])
    elif mode==1:
        nStr, nDex, nInt, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0
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
            sprint('Level:', pStats['lvl'])
            sprint('\nExp:', pStats['xp'])
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
        if save==1 and os.path.isfile('do-not-touch.dat') == True:
            with open('do-not-touch.dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save==2 and os.path.isfile('do-not-touch(1).dat') == True:
            with open('do-not-touch(1).dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save==3 and os.path.isfile('do-not-touch(2).dat') == True:
            with open('do-not-touch(2).dat', 'rb') as f:
                player = pickle.dump(f)
                print ("\nGame has been loaded!\n")
        elif save==4 and os.path.isfile('do-not-touch(3).dat') == True:
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

def playerTakeDmg(attacker, defender):
    dmg = random.randint(attacker['stats']['atk'][0], \
                         attacker['stats']['atk'][1])
    defender['stats']['hp'] -= dmg
    if defender['stats']['hp'] <= 0:
        sprint('{} has been slain.\n'.format(defender['name']))
        if defender == hero:
            player['stats']['lives'] -= 1
            sprint('You died!\n')
            if hero['stats']['lives'] > 0:
                sprint('Would you like to continue? Y/')
                gameover = input('N ').lower()
                if gameover == 'y':
                    load()
                if gameover == 'n':
                    sprint('Game Over!\n')
                    time.sleep(5)
                    if 'idlelib.run' in sys.modules:
                        sprint('\n############################\n\n')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    start()
            elif hero['stats']['lives'] == 0:
                sprint('Game Over!\nYou ran out of lives!\n')
                sprint('Exiting to title screen...\n')
                time.sleep(2.5)
                start()
    sprint('{} takes {} damage!\n'.format(defender['name'], dmg))
    commands(defender, attacker)

def takeDmgextra(attacker, defender):
    dmgprecursor = random.randint(attacker['stats']['atk'][0], \
                         attacker['stats']['atk'][1])
    dmg = 1 + (random.randint(attacker['atkplus'][0], attacker['atkplus'][1]) / 100) * dmgprecursor + dmgprecursor
    defender['stats']['hp'] -= dmg
    if defender['stats']['hp'] <= 0:
        sprint('{} has been slain.\n'.format(defender['name']))
        if defender == hero:
            player['stats']['lives'] -= 1
            sprint('You died!\n')
            if hero['stats']['lives'] > 0:
                sprint('Would you like to continue? Y/')
                gameover = input('N ').lower()
                if gameover == 'y':
                    load()
                if gameover == 'n':
                    sprint('Game Over!\n')
                    time.sleep(5)
                    if 'idlelib.run' in sys.modules:
                        sprint('\n############################\n\n')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    start()
            elif hero['stats']['lives'] == 0:
                sprint('Game Over!\nYou ran out of lives!\n')
                sprint('Exiting to title screen...\n')
                time.sleep(2.5)
                start()
    sprint('{} takes {} damage!\n'.format(defender['name'], dmg))
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
        sprint('{} has been slain.\n'.format(defender['name']))
        if defender == hero:
            player['stats']['lives'] -= 1
            sprint('You died!\n')
            if hero['stats']['lives'] > 0:
                sprint('Would you like to continue? Y/')
                gameover = input('N ').lower()
                if gameover == 'y':
                    load()
                if gameover == 'n':
                    sprint('Game Over!\n')
                    time.sleep(5)
                    if 'idlelib.run' in sys.modules:
                        sprint('\n############################\n\n')
                    else:
                        os.system('cls' if os.name == 'nt' else 'clear')
                    start()
            elif hero['stats']['lives'] == 0:
                sprint('Game Over!\nYou ran out of lives!\n')
                sprint('Exiting to title screen...\n')
                time.sleep(2.5)
                start()
        if attacker == hero:
            if defender == ghost:
                if attacker['pets']['slot1'] == 'empty':
                        attacker['pets']['slot1'] = defender['reward']
                        sprint('You\'ve obtained {}!\n'.format(defender['reward']))
                if attacker['pets']['slot1'] != 'empty':
                    for slots in attacker['pets']:
                        if slot in slots == 'empty':
                            slot = defender['reward']
                    sprint('You\'ve obtained {}!\n'.format(defender['reward']))
                    attacker['xp'] += defender['xpreward']
                    level(attacker)
            if defender == dragon:
                    if attacker['items']['slot1'] == 'empty':
                        random.shuffle(dragon['reward'])
                        attacker['items']['slot1'] = defender['reward'][0]
                        sprint('You\'ve obtained {}!\n'.format(defender['reward'[0]]))
                    if attacker['items']['slot1'] != 'empty':
                        for slots in attacker['items']:
                            if slot in slots == 'empty':
                                slot = defender['reward']
                        sprint('You\'ve obtained {}!\n'.format(defender['reward']))
                        attacker['xp'] += defender['xpreward']
                        level(attacker)
            if attacker['items']['slot1'] == 'empty':
                attacker['items']['slot1'] = defender['reward']
                sprint('You\'ve obtained {}!\n'.format(defender['reward']))
            for slots in attacker['items']:
                if slot in slots == 'empty':
                    slot = defender['reward']
            sprint('You\'ve obtained {}!\n'.format(defender['reward']))
            attacker['xp'] += defender['xpreward']
            level(attacker)
    else:
        sprint('{} takes {} damage!\n'.format(defender['name'], dmg))
        commands(attacker, defender)

def commands(knight, enemy):
    sprint('You\'ve run into a(n) {}!!!\n'.format(enemy['name']))
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
                sprint('{} takes the opportunity to attack {}!\n'.format(enemy['name'], knight['name']))
                playerTakeDmg(enemy, knight)
        else:
            commands(knight, enemy)
    while True:
        if a == 5:
            sprint('{} takes the opportunity to attack the {} with extra power!\n'.format(enemy['name'], knight['name']))
            takeDmgextra(enemy, knight)

#

def spells(know): #activate with "spells(player['stats']['int'])
    if know >= 25:
        sprint('Would you like to cast a heal, power, or money spell')
        cast = input("? ").lower()
        if cast == 'yes':
            sprint('Power, Money, or Heal')
            choose = input('? ').lower()
            if choose == 'power':
                player["stats"]['str'] + 10
                player['stats']['atk'][1] + 5
                player['stats']['hp'] - 20
                pass
            if choose == 'heal':
                player['stats']['str'] - 5
                player['stats']['hp'] + 10
                if player['stats']['hp'] > player['stats']['maxHp']:
                    player['stats']['hp'] = player['stats']['maxHp']
                pass
            if choose == 'money':
                player['stats']['str'] - 5
                player['stats']['dex'] - 5
                amount = random.randint[(5*(player['lvl'])), (10*(player['lvl']))]
                currencies=['jewels', 'crowns', 'doubloons']
                random.shuffle(currencies)
                x=currencies[0]
                player['stats'][x] + amount
                pass
        if cast == 'no':
            pass
    if know >= 10:
        sprint('Would you like to cast a heal or power spell')
        cast = input("? ").lower()
        if cast == 'yes':
            sprint('Power or Heal')
            choose = input('? ').lower()
            if choose == 'power':
                player["stats"]['str'] + 5
                player['stats']['atk'][1] + 3
                player['stats']['hp'] - 10
                pass
            if choose == 'heal':
                player['stats']['str'] - 1
                player['stats']['hp'] + 1
                if player['stats']['hp'] > player['stats']['maxHp']:
                    player['stats']['hp'] = player['stats']['maxHp']
                pass
        if cast == 'no':
            pass
    if know >= 5:
        sprint('Would you like to cast a basic heal spell')
        cast = input("? ").lower()
        if cast == 'no':
            pass
        if cast == 'yes':
            player['stats']['str'] - 1
            player['stats']['hp'] + 1
            if player['stats']['hp'] > player['stats']['maxHp']:
                player['stats']['hp'] = player['stats']['maxHp']
            pass
    sprint(player['stats'])

def altBattle(stage, enemy):
    ice_sorceress = {'name' : 'Ice sorceress',
                      'lvlRange' : [6, 23], #level
                      'lvl' : 0,
                      'atkplus' : [3, 11], # %boost on atk
                      'xpreward' : [2, 14],
                      'stats' : {'str' : 3, #strength
                             'dex' : 1, #dexterity or skill
                             'int' : 2, #intelligence
                             'hp' : 0, #depend on lvl
                             'atk' : [5, 13]}} #attack power
    iron_knight = {'name' : 'Iron knight',
          'lvl' : [12, 28], #level
          'atkplus' : [9, 14], # %boost on atk
          'reward' : 'the Knight\'s chestpiece', #reward for slaying
          'xpreward' : [20, 51],
          'stats' : {'str' : 18, #strength
                 'dex' : 14, #dexterity or skill
                 'int' : 6, #intelligence
                 'hp' : 0, #depend on lvl
                 'atk' : [14, 31]}} #attack power
    golem = {'name' : 'Gem golem',
          'lvlRange' : [7, 13],  #level
          'lvl' : 0,
          'atkplus' : [5, 16], # %boost on atk
          'reward' : 'Ruby leggings', #reward for slaying
          'xpreward' : [12, 15],
          'stats' : {'str' : 12, #strength
                 'dex' : 5, #dexterity or skill
                 'int' : 3, #intelligence
                 'hp' : 0, #health
                 'atk' : [9, 15]}} #attack power
    dragon = {'name' : 'Crystal dragon',
          'lvl' : 75, #level
          'atkplus' : [40, 65], # %boost on atk
          'reward' : ['Helm of the Crystal Menace'], #reward for slaying
          'xpreward' : [10000, 25000],
          'stats' : {'str' : 605, #strength
                 'dex' : 20, #dexterity or skill
                 'int' : 50, #intelligence
                 'hp' : 56250, #health
                 'atk' : [5250, 6750]}} #attack power
    ghost = {'name' : 'Legendary ghoul',
          'lvl' : 11, #level
          'atkplus' : [7, 13], # %boost on atk
          'reward' : 'Ring of Possession', #reward for slaying
          'xpreward' : [30, 30.5],
          'stats' : {'str' : 7, #strength
                 'dex' : 0, #dexterity or skill
                 'int' : 5, #intelligence
                 'hp' : 25, #health
                 'atk' : [14, 23]}} #attack power
    arrow_master = {'name' : 'Archer of Fate',
          'lvlRange' : [15, 30], #level
          'lvl' : 0,
          'atkplus' : [10, 40], # %boost on atk
          'reward' : 'Boots of Xerxes', #reward for slaying
          'xpreward' : [10000, 15000],
          'stats' : {'str' : 5000, #strength
                 'dex' : 500, #dexterity or skill
                 'int' : 500, #intelligence
                 'hp' : 0,
                 'atk' : [500, 700]}} #attack power
    enemy['lvl'] = random.randint(enemy['lvlRange'][0], enemy['lvlRange'][1])
    if enemy['lvl'] > (stage + 9):
        enemy['lvl'] = (stage + 9)
    if enemy=='ice_sorceress':
        ice_sorceress['stats']['hp'] = ice_sorceress['lvl']*50
    if enemy=='iron_knight':
        iron_knight['stats']['hp'] = iron_knight['lvl']*2
    if enemy=='golem':
        golem['stats']['hp']+=golem['lvl']*8
    if enemy=='arrow_master':
        arrow_master['stats']['hp']+=arrow_master['lvl']*37500
    sprint('A(n) ' + enemy['name'] + ' challenges you!\n')

def serum():
    pass

b=0
c=0
DevMode=0
thirteenKnightMode=0
ModernMode=0

def start():
    global a
    a=0
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
    try:
        start()
    except KeyboardInterrupt:
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
        old_memory_intro = '''Some time ago...\nI knew a knight, but at the time, as a friend.\
\nHe saw a poster for knights to scour the kingdom to find the mighty Blanghthorn\
 and slay it.\nBlinded by the prize money, he signed a contract, saying he would give\
 his life for the royal family...\n'''
        for letter in old_memory_intro:
            sys.stdout.write(letter)
            sys.stdout.flush()
            time.sleep(.08)
        time.sleep(1.5)
        sprint('This..is....\n')
        time.sleep(1.5)
        sprint('their tale......\n')
        while player['gameOver'] == 0:
            try:
                prompt()
            except KeyboardInterrupt:
                prompt()
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
                sprint('Entering the tournament...\n')
                time.sleep(1.5)
                sprint('You arrive at the tournament.\nYou proceed to the first stage.\n')
                altPlayer['stage']=1
                altBattle(1, ice_sorceress)
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
                    hero['lives']=5
                    sprint('Hp has been set to 50/50,\nAtk range has been set from 5 to 15.\nAvailable lives set to 5.\n')
                elif diff=='2':
                    hero['maxHp']=30
                    hero['hp']=hero['maxHp']
                    hero['atk']=[2, 12]
                    hero['lives']=3
                    sprint('Hp has been set to 30/30,\nAtk range has been set from 2 to 12.\nAvailable lives set to 3.')
                elif diff=='3':
                    hero['maxHp']=10
                    hero['hp']=hero['maxHp']
                    hero['atk']=[0, 9]
                    hero['lives']=1
                    sprint('Hp has been set to 10/10,\nAtk range has been set from 0 to 9.\nAvailable lives set to 1.')
                b=0
                time.sleep(.5)
                clear()
                start()
            except ValueError:
                a=3
                b=0
                sprint('Err: UnknownDifficultySetting. Attempt again.\n')
                clear()
        elif settingedit=='back':
            a=0
            b=0
            clear()
            start()
        else:
            a=3
            b=0
            sprint('Err: UnknownOption. Attempt again.\n')
            clear()
    elif (a==4 and thirteenKnightMode==0) or (a==3 and thirteenKnightMode==1):
        sprint('|Buy DLC|Enter Code|Disable Codes')
        bonus=input('| ').lower()
        if bonus=='buy dlc' and thirteenKnightMode==0:
            b=1
            a=0
            sprint('You must load an existing a game or create a new one to continue. Continue? Y/N')
            loadornot=input(' ').lower()
            if loadornot=='n':
                b=0
                a=4
            elif loadornot=='y':
                load()
                sprint('DLC List:\n-Legend Armor-   -7500-\n-Resurrection Spell Recipe-   -5000-\n\n')
                sprint('Enter wanted DLC')
                content=input(': ').lower()
                while content not in dlcCost:
                   sprint('Unknown option try again.')
                   sprint('Enter wanted DLC')
                   content=input(': ')
                sprint('Cost: ')
                print (dlcCost[content])
                sprint('\nAre you sure you want purchase this? Y/N')
                confirm=input(' ').lower()
                if confirm=='n':
                    sprint('\nCancelling purchase...\n')
                    time.sleep(2)
                elif confirm=='y':
                    sprint('Charging account...\n')
                    time.sleep(1)
                    if megaGems < dlcCost[content]:
                        sprint('Not enough Mega Gems.\nThese are not fully implemented yet.')
                    elif megaGems >= dlcCost[content]:
                        megaGems -= dlcCost[content]
                        sprint(megaGems + ' Mega Gems left.\n')
                        sprint('You have bought ')
                        sprint(dlcCost[content])
                        sprint('!\n')
                else:
                    sprint('Unknown option.')
                    time.sleep(.4)
                    b=0
                    a=4
                b=0
                clear()
                start()
            else:
                sprint('Unknown option.')
                time.sleep(.4)
                b=0
                a=4
                clear()
                start()
            b=0
            clear()
            start()
        elif bonus=='enter code':
            a=0
            b=1
            sprint('Enter code')
            diff=input(': ')
            if diff=='DevMode':
                if thirteenKnightMode==0:
                    sprint('CODE INSERTED SUCCESSFULLY. \"DEVELOPER TOOLS\" ADDED TO TITLE SCREEN.\n')
                    time.sleep(.8)
                    sprint('YOU CAN ENTER "UNDEV()" INTO THE DEVELOPER TERMINAL TO EXIT DEVMODE.\n')
                    DevMode=1
                    b=0
                    time.sleep(2.5)
                    clear()
                    start()
                elif thirteenKnightMode==1:
                    sprint('CODE INTERFERED WITH ANOTHER CODE.\nWOULD YOU LIKE TO DISABLE THE OTHER CODE? Y/')
                    i=input('N ').lower()
                    if i=='n':
                        sprint('CODE NOT INSERTED.\nDISABLE INTERFERING CODE TO ENABLE DEVELOPER MODE.\n')
                        b=0
                        start()
                    elif i=='y':
                        sprint('DISABLING INTERFERING CODE...')
                        time.sleep(.5)
                        sprint('INSERTING NEW CODE.\nCODE INSERTED SUCCESSFULLY. \"DEVELOPER TOOLS\" ADDED TO TITLE SCREEN.\n')
                        time.sleep(.8)
                        sprint('YOU CAN ENTER "UNDEV()" INTO THE DEVELOPER TERMINAL TO EXIT DEVMODE.\n')
                        DevMode=1
                        thirteenKnightMode=0
                        b=0
                        time.sleep(5)
                        clear()
                        start()
            elif diff=='ThirteenthKnight':
                if DevMode==0:
                    sprint('CODE INSERTED SUCCESSFULLY. \"THIRTEENTH KNIGHT MODE\" UNLOCKED.\n')
                    thirteenKnightMode=1
                    b=0
                    time.sleep(2.5)
                    clear()
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
                        clear()
                        start()
            elif diff=='ModernMode':
                sprint('CODE INSERTED SUCCESSFULLY. A modernized version has appeared when starting a new game\n')
                ModernMode=1
                b=0
                time.sleep(3)
                clear()
                start()
            else:
                sprint('CODE REJECTED. INSERT VALID CODE.\n')
                clear()
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
                clear()
                start()
            elif ModernMode==1 or DevMode==1 or thirteenKnightMode==1:
                sprint('DISABLING ALL CODES...\n')
                time.sleep(1.2)
                ModernMode=0
                DevMode=0
                thirteenKnightMode=0
                b=0
                clear()
                start()
        else:
            b=0
            a=4
            sprint('Err: UnknownOption. Re-Attempt.\n')
            clear()
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
        sprint('-CHEATS\n')
        time.sleep(.4)
        sprint('-MORE TOOLS COMING SOON!-\n')
        t=input('~ ').lower()
        if t=='terminal':
            sys.exit()
        elif t=='debug':
            import pdb; pdb.set_trace()
        elif t=='help':
            sprint('DEVELOPER MODE HELP TOOL\n    TERMINAL-\n        THE STANDARD PROMPT WHEN USING THE PYTHON SHELL.\
\n\n    DEBUG-\n        A DEBUG MODE USING THE PDB MODULE. EXITS INTO THE TERMINAL.\n        NOT RECOMMENDED FOR AMATEURS.\n\n    CHEATS-\n        A COLLECTION OF CHEATS TO HELP YOUR JOURNEY.\n')
            a=5
            b=0
            time.sleep(10)
            clear()
        elif t=='cheats':
            sprint('CHEAT LIST:\n')
            time.sleep(.3)
            sprint('-MONEY CONTROLS\n')
            time.sleep(.4)
            sprint('-PORTAL ON/OFF\n')
            c=input('~ ').lower()
            if c=='money controls':
                sprint('What currency would you like to change?\nCrowns\nDoubloons\nJewels\nMega Gems\n')
                m=input('~ ').lower()
                if m=='crowns':
                    sprint('What value would you like to set your crowns to?')
                    crowns = input(' ')
                    try:
                        x=int(crowns)
                        player['crowns'] = crowns
                    except ValueError:
                        while int(crowns) == ValueError:
                            sprint('Enter a valid number please.\n')
                            sprint('What value would you like to set your crowns to?')
                            crowns=input(' ')
                        player['crowns'] = crowns
                elif m=='doubloons':
                    sprint('What value would you like to set your doubloons to?')
                    doubloons = input(' ')
                    try:
                        x=int(doubloons)
                        player['doubloons'] = doubloons
                    except ValueError:
                        while int(doubloons) == ValueError:
                            sprint('Enter a valid number please.\n')
                            sprint('What value would you like to set your doubloons to?')
                            doubloons=input(' ')
                        player['doubloons'] = doubloons
                elif m=='jewels':
                    sprint('What value would you like to set your jewels to?')
                    jewels = input(' ')
                    try:
                        x=int(jewels)
                        player['jewels'] = jewels
                    except ValueError:
                        while int(jewels) == ValueError:
                            sprint('Enter a valid number please.\n')
                            sprint('What value would you like to set your jewels to?')
                            jewels=input(' ')
                        player['jewels'] = jewels
                elif m=='mega gems':
                    sprint('What value would you like to set your Mega Gems to?')
                    megaGems = input(' ')
                    try:
                        x=int(megaGems)
                        player['megaGems'] = megaGems
                    except ValueError:
                        while int(megaGems) == ValueError:
                            sprint('Enter a valid number please.\n')
                            sprint('What value would you like to set your megaGems to?')
                            megaGems=input(' ')
                        player['megaGems'] = megaGems
            elif c=='portal on/off':
                zone1['d2']['solved'] = not zone1['d2']['solved']
            else:
                sprint('ERR: UNKNOWNOPTION. ATTEMPT AGAIN.\n')
            clear()
            t='cheats'
            a=5
            b=0
        else:
            sprint('ERR: UNKNOWNOPTION. ATTEMPT AGAIN.\n')
            clear()
            a=5
            b=0
    else:
        b=0
        a=0
        sprint('Invalid Value. Choose a listed option please.\n')
        start()
