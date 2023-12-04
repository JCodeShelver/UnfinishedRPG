#------------------------------------------------- chest code -------------------------------------------------#
from DefaultHero import *

class keychest:

    def __init__(self):
        self.castleChest = 'closed'
        self.starterChest = 'closed'
        self.prisonChest = 'closed'
        self.MLGChest = 'closed'

    def openChest(self, chestType):
        if (chestType == 'castleChest'):
            self.castleChest = 'open'
        elif (chestType == 'starterChest'):
            self.starterChest = 'open'
        elif (chestType == 'prisonChest'):
            self.prisonChest = 'open'
        elif (chestType == 'MLGChest'):
            self.MLGChest = 'open'

    def keyChestLoot(self, chestType):
        if (chestType == 'castleChest'):
            return ''
        elif (chestType == 'starterChest'):
            return ''
        elif (chestType == 'prisonChest'):
            return 'bloodandbone trophy'
        elif (chestType == 'MLGChest'):
            return ''

    def chestLock(self, chestType):
        chestTypeLock = eval('self.' + chestType)
        if chestTypeLock == True and player['']:
            pass

    def chestKey(chestLock):
        pass

class crate(keychest):
    pass
