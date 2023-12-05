from DefaultHero import player as player
from Utils import sprint

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

def level(pStats, mode=0):                  #enter 'player' or 'hero' inside of peremeter 1, mode perameter is a secret
    if mode == 0:
        if pStats['lvl'] > 250:
            pStats['lvl'] = 250
            pStats['xp'] = -1
            pStats['lvlNext'] = -1
        elif pStats['lvl'] == 250:
            sprint('Sorry, you are already at the max level.\n')
        else:
            nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, [0, 0]
            while pStats['xp'] >= pStats['lvlNext'] and pStats['lvl'] < 250:
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
            sprint((f'Stats: STRENGTH {pStats["stats"]["str"]} +{nStr}, \n'
                   f'DEXTERITY {pStats["stats"]["dex"]} +{nDex}, \n'
                   f'INTELLIGENCE {pStats["stats"]["int"]} +{nInt}, \n'
                   f'HEALTH {pStats["stats"]["hp"]} +{nHp}, \n'
                   f'ATTACK {pStats["stats"]["atk"][0]}, {pStats["stats"]["atk"][1]} +{nAtkDmg[0]}, {nAtkDmg[1]}, \n'
                   f'MAGIC {pStats["stats"]["mag"]} +{nMag}\n'))
            pStats['stats']['atk'][0] += nAtkDmg[0]
            pStats['stats']['atk'][1] += nAtkDmg[1]
            pStats['stats']['hp'] += nHp
            pStats['stats']['maxHp'] += nMaxHp
            pStats['stats']['str'] += nStr
            pStats['stats']['dex'] += nDex
            pStats['stats']['int'] += nInt
            pStats['stats']['mag'] += nMag
            sprint((f'Exp left required to gain a level:\n {pStats["lvlNext"] - pStats["xp"]}\n'
                    f'Exp required total to gain level:\n {pStats["lvlNext"]}\n'
                     '------------------------------\n'))
            nStr, nDex, nInt, nMag, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, 0, [0, 0]
            atkUnlocks(pStats['lvl'])
    elif mode==1:
        nStr, nDex, nInt, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, [0, 0]

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
            sprint((f'Level: {pStats["lvl"]}\n'
                    f'Exp: {pStats["xp"]}\n'
                     'Stats:\n'
                    f'     Str: {nStr}\n'
                    f'     Dex: {nDex}\n'
                    f'     Int: {nInt}\n'
                    f'     Health: {nHp}\n'
                    f'     Atk: {nAtkDmg[0]}-{nAtkDmg[1]}\n'))

            pStats['stats']['atk'][0] += nAtkDmg[0]
            pStats['stats']['atk'][1] += nAtkDmg[1]
            pStats['stats']['hp'] += nHp
            pStats['stats']['maxHp'] += nMaxHp
            pStats['stats']['str'] += nStr
            pStats['stats']['dex'] += nDex
            pStats['stats']['int'] += nInt
            nStr, nDex, nInt, nHp, nMaxHp, nAtkDmg = 0, 0, 0, 0, 0, [0, 0]
    elif mode==2:
        pass