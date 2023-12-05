b=0
c=0
DevMode=0
boss_rush=0
ModernMode=0
from Utils import sprint

title_menu_sel = 0
def start():
    global title_menu_sel
    if boss_rush==1:
        sprint('-----The Thirteenth Knight-----\n1) New Game\n2) Settings\n3) Bonus Content\n-------------------------------\n')
        Selection = input('> ')
        try:
            title_menu_sel=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            sprint ('\n############################\n\n')
            start()
    else:
        sprint('-----The Twelfth Knight-----\n1) New Game\n2) Load Game\n3) Settings\n4) Bonus Content\n----------------------------\n')
        Selection = input('> ')
        try:
            title_menu_sel=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            sprint ('\n############################\n\n')
            start()

from SaveLoad import *
import sys
import time
from Battle import *
from Chest import *
from EnemyList import *
from LevelUp import *

start()
while b==0:
    if title_menu_sel == 1 and boss_rush==0:
        b=1
        title_menu_sel=0
        from DefaultHero import player as player

        sprint('Enter the chosen one\'s name: ')
        name = input()
        player['name'] = name

        sprint('Choose your primary talent: |Mage|Healer|Soldier|Scientist| ')
        role=input().lower()
        player['role'] = role

        if role=='mage':
            sprint('You have become a mage!\nYou magical abilities are growing!\nAs the magic flows \
through you, you get more powerful!\nMagic increased to 5!\n')
            player['stats']['mag'] = 5
        elif role=='healer':
            sprint('You have become a healer!\nYou medical abilities are growing!\nAs you help more \
people, you get more skills!\nHealth increased to 35!\n')
            player['stats']['hp'] = 35
            player['stats']['maxHp'] = 35
        elif role=='soldier':
            sprint('You have become a soldier!\nYou attacking capabilities are growing!\nAs your sword slashes \
through your oppenents, you get more skilled!\nSpeed, Strength, and Dexterity increased to 5!\n')
            player['stats']['str'] = 5
            player['stats']['dex'] = 5
            player['stats']['speed'] = 5
        elif role=='scientist':
            sprint('You have become a scientist!\nYou chemical abilities are growing!\nAs the knowledge floods \
your mind, you get smarter!\nIntelligence increased to 5!\n')
            player['stats']['int'] = 5
        else:
            b=0
            title_menu_sel=1
    elif title_menu_sel==1 and boss_rush==1:
        b=1
        title_menu_sel=0
        from AlternateDefaultHero import altPlayer as player
        from AlternateEnemyList import *
        from AlternateTournament import *
        sprint('Enter the chosen one\'s name: ')
        name=input()
        player['name'] = name

        sprint('13 Knight Mode is a short, EXTREME, tournament of battles.\nAre you sure you want to proceed? Y/N ')
        t=input().lower()
        if t=='n':
            sprint('13 Knight Mode will be deactivated.\nYou can reactivate it buy entering the code again.\n')
            boss_rush=0
            b=0
            start()
        elif t=='y':
            sprint('YOU CANNOT SAVE. There are 50 levels in all.\nAre you really sure you want to proceed? Y/N')
            confirm=input().lower()
            if confirm=='y':
                sprint('Entering the tournament...\n')
                time.sleep(1.5)
                with open('AlternateTournament.py') as file:
                    exec(file.read())
            if confirm=='n':
                sprint('13 Knight Mode will be deactivated.\nYou can reactivate it buy entering the code again.\n')
                boss_rush=0
                b=0
                start()
    elif title_menu_sel==2 and boss_rush==0:
        try:
            b=1
            title_menu_sel=0
            load()
        except FileNotFoundError:
            title_menu_sel=0
            b=0
            sprint('> No Save file found\n')
            time.sleep(.2)
            sprint ('\n############################\n\n')
            start()
    elif (title_menu_sel==3 and boss_rush==0) or (title_menu_sel==2 and boss_rush==1):
        title_menu_sel=0
        b=1
        sprint('Choose what setting to change: |Back|Dialogue Speed|Difficulty')
        settingedit=input('| ').lower()
        if settingedit=='dialogue speed':
            sprint('What speed should dialogue be spoken?\nSlowest is 1, Fastest is 3')
            sps=input('. ').strip()
            try:
                from Utils import setSprintSpeed
                if int(sps)>=3:
                    setSprintSpeed(0.01)
                elif int(sps)<=1:
                    setSprintSpeed(0.1)
                elif int(sps)==2:
                    setSprintSpeed(0.04)
                b=0
                time.sleep(.5)
                start()
            except ValueError:
                title_menu_sel=3
                b=0
                sprint('Err: UnknownSpeedValue. Attempt again.\n')
                sprint ('\n############################\n\n')
        elif settingedit=='difficulty' and boss_rush==0:
            sprint('What should be set? 1-3')
            diff=input()
            try:
                if diff=='1':
                    player['maxHp']=50
                    player['hp']=player['maxHp']
                    player['atk']=[5, 15]
                    sprint('Hp has been set to 50/50,\nAtk range has been set from 5 to 15..\n')
                elif diff=='2':
                    player['maxHp']=30
                    player['hp']=player['maxHp']
                    player['atk']=[2, 12]
                    sprint('Hp has been set to 30/30,\nAtk range has been set from 2 to 12.\n')
                elif diff=='3':
                    player['maxHp']=10
                    player['hp']=player['maxHp']
                    player['atk']=[0, 9]
                    sprint('Hp has been set to 10/10,\nAtk range has been set from 0 to 9.\n')
                b=0
                time.sleep(.5)
                sprint ('\n############################\n\n')
                start()
            except ValueError:
                title_menu_sel=3
                b=0
                sprint('Err: UnknownDifficultySetting. Attempt again.\n')
                sprint ('\n############################\n\n')
        elif settingedit=='back':
            title_menu_sel=0
            b=0
            sprint('\n############################\n\n')
            start()
        else:
            title_menu_sel=3
            b=0
            sprint('Err: UnknownOption. Attempt again.\n')
            sprint ('\n############################\n\n')
    elif (title_menu_sel==4 and boss_rush==0) or (title_menu_sel==3 and boss_rush==1):
        sprint('|Buy DLC|Enter Code|Disable Codes')
        bonus=input('| ').lower()
        if bonus=='buy dlc':
            b=1
            title_menu_sel=0
            sprint('No DLC available yet. :(\n')
            b=0
            sprint ('\n############################\n\n')
            start()
        elif bonus=='enter code':
            title_menu_sel=0
            b=1
            sprint('Enter code')
            diff=input(': ')
            if diff=='ThirteenthKnight':
                sprint('CODE INSERTED SUCCESSFULLY. \"THIRTEENTH KNIGHT MODE\" UNLOCKED.\n')
                boss_rush=1
                b=0
                sprint('\n############################\n\n')
                start()
            else:
                sprint('CODE REJECTED. INSERT VALID CODE.\n')
                sprint('\n############################\n\n')
                if boss_rush==0:
                    title_menu_sel=4
                elif boss_rush==1:
                    title_menu_sel=3
                b=0
        elif bonus=='disable codes':
            b=1
            title_menu_sel=0
            if boss_rush==0:
                sprint('NO CODES TO DISABLE. HAVE A NICE DAY.\n')
                b=0
                sprint('\n############################\n\n')
                start()
            elif boss_rush==1:
                sprint('DISABLING ALL CODES...\n')
                time.sleep(1.2)
                boss_rush=0
                b=0
                sprint('\n############################\n\n')
                start()
        else:
            b=0
            title_menu_sel=4
            sprint('Err: UnknownOption. Re-Attempt.\n')
            sprint('\n############################\n\n')
    else:
        b=0
        title_menu_sel=0
        sprint('Invalid Value. Choose a listed option please.\n')
        start()
