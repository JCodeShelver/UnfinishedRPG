import random

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
