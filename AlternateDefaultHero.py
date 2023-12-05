altPlayer = {
    'lvl' : 1, #level
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
