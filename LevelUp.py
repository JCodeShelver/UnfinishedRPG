from DefaultHero import *
from Testing import sprint
import sys
##This file is for the leveling up of the player,
##and the attacks they unlock on the way.


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

def level(pStats):                  #enter 'player' or 'hero' inside of peremeter
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
        sprint('Level:\n', pStats['lvl'])
        sprint('Exp:\n', pStats['xp'])
        sprint('Stats: STRENGTH {} +{}, DEXTERITY {} +{}, INTELLIGENCE {} +{}, HEALTH {} +{}, ATTACK {}, {} +{}, {}, MAGIC {} +{}\n'.format(pStats['stats']['str'], nStr,
                                                                                                                   pStats['stats']['dex'], nDex,
                                                                                                                   pStats['stats']['int'], nInt,
                                                                                                                   pStats['stats']['hp'], nHp,
                                                                                                                   pStats['stats']['atk'][0], pStats['stats']['atk'][1],
                                                                                                                   nAtkDmg[0], nAtkDmg[1], pStats['stats']['mag'], nMag))
        pStats['stats']['atk'][0] += nAtkDmg[0]
        pStats['stats']['atk'][1] += nAtkDmg[1]
        pStats['stats']['hp'] += nHp
        pStats['stats']['str'] += nStr
        pStats['stats']['dex'] += nDex
        pStats['stats']['int'] += nInt
        pStats['stats']['mag'] += nMag
        sprint('Exp left required to gain a level:\n ', pStats['lvlNext'] - pStats['xp'])
        sprint('Exp required total to gain level:\n ', pStats['lvlNext'])
        nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, 0
        sprint('------------------------------\n')
        atkUnlocks(pStats['lvl'])
