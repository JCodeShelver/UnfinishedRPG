import os
import pickle
import random
import sys
import time
from Utils import sprint, setSprintSpeed
from DefaultHero import player as player
from SaveLoad import save, load
from LevelUp import level
from EnemyList import *

# with open('mDoc.dat', 'rb') as m:
    # megaGems=pickle.load(m)
megaGems = 0
dlcCost = {'legend armor' : 7500,
           'resurrection spell recipe' : 5000}

title_menu_sel = 0
b=0
c=0
boss_rush_mode=0

from Utils import clearScreen

def mainMenu():
    global title_menu_sel
    if boss_rush_mode==1:
        sprint('-----The Thirteenth Knight-----\n1) New Game\n2) Settings\n3) Bonus Content\n-------------------------------\n')
        selection = input('> ')
        try:
            title_menu_sel=int(selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            clearScreen()
            mainMenu()
    else:
        sprint('-----The Twelfth Knight-----\n1) New Game\n2) Load Game\n3) Settings\n4) Bonus Content\n----------------------------\n')
        selection = input('> ')
        try:
            title_menu_sel=int(selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            clearScreen()
            mainMenu()

if 'idlelib.run' not in sys.modules:
    os.system('cls' if os.name == 'nt' else 'clear')
mainMenu()

while b==0:
    if title_menu_sel==1 and boss_rush_mode==0:
        b=1
        title_menu_sel=0
        sprint('Enter the chosen one\'s name: ')
        name=input()
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
    elif title_menu_sel==1 and boss_rush_mode==1:
        b=1
        title_menu_sel=0
        sprint('Enter the chosen one\'s name: ')
        name=input()
        player['name'] = name

        sprint('13 Knight Mode is a short, EXTREME, tournament of battles.\nAre you sure you want to proceed? Y/N ')
        t=input().lower()
        if t=='n':
            sprint('13 Knight Mode will be deactivated.\nYou can reactivate it buy entering the code again.\n')
            boss_rush_mode=0
            b=0
            mainMenu()
        elif t=='y':
            sprint('YOU CANNOT SAVE. There are 50 levels in all.\nAre you really sure you want to proceed? Y/')
            confirm=input('N ').lower()
            if confirm=='y':
                with open("AlternateTournament.py") as file:
                    exec(file.read())
            if confirm=='n':
                sprint('13 Knight Mode will be deactivated.\nYou can reactivate it buy entering the code again.\n')
                boss_rush_mode=0
                b=0
                mainMenu()
    elif title_menu_sel==2 and boss_rush_mode==0:
        try:
            b=1
            title_menu_sel=0
            load()
        except FileNotFoundError:
            title_menu_sel=0
            b=0
            sprint('> No Save file found\n')
            time.sleep(.2)
            clearScreen()
            mainMenu()
    elif (title_menu_sel==3 and boss_rush_mode==0) or (title_menu_sel==2 and boss_rush_mode==1):
        title_menu_sel=0
        b=1
        sprint('Choose what setting to change: |Back|Dialogue Speed|Difficulty')
        settingedit=input('| ').lower()
        if settingedit=='dialogue speed':
            sprint('What speed should dialogue be spoken?\nSlowest is 1, Fastest is 3')
            sps=input('. ')
            try:
                if int(sps)>=3:
                    setSprintSpeed(.01)
                elif int(sps)<=1:
                    setSprintSpeed(.1)
                elif int(sps)==2:
                    setSprintSpeed(.04)
                b=0
                time.sleep(.5)
                mainMenu()
            except ValueError:
                title_menu_sel=3
                b=0
                sprint('Err: UnknownSpeedValue. Attempt again.\n')
                clearScreen()
        elif settingedit == 'difficulty' and boss_rush_mode == 0:
            sprint('What should be set? 1-3 ')
            diff = input()
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
                clearScreen()
                mainMenu()
            except ValueError:
                title_menu_sel=3
                b=0
                sprint('Err: UnknownDifficultySetting. Attempt again.\n')
                clearScreen()
        elif settingedit=='back':
            title_menu_sel=0
            b=0
            clearScreen()
            mainMenu()
        else:
            title_menu_sel=3
            b=0
            sprint('Err: UnknownOption. Attempt again.\n')
            clearScreen()
    elif (title_menu_sel==4 and boss_rush_mode==0) or (title_menu_sel==3 and boss_rush_mode==1):
        sprint('|Buy DLC|Enter Code|Disable Codes')
        bonus=input('| ').lower()
        if bonus=='buy dlc':
            b=1
            title_menu_sel=0
            sprint('DLC List:\n-Legend Armor-   -7500-\n-Resurrection Spell Recipe-   -5000-\n\n')
            sprint('Enter wanted DLC: ')
            content=input().lower()
            sprint(f'Cost: {dlcCost[content]}\n')
            sprint('Are you sure you want purchase this? Y\\N ')
            confirm = input().lower()
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
                        spend = input()

                elif megaGems >= dlcCost[content]:
                    megaGems -= dlcCost[content]
                    sprint(str(megaGems) + ' Mega Gems left.')
            b=0
            clearScreen()
            mainMenu()
        elif bonus == 'enter code':
            title_menu_sel = 0
            b = 1
            sprint('Enter code')
            diff = input(': ')
            if diff == 'ThirteenthKnight':
                sprint('CODE INSERTED SUCCESSFULLY. \"THIRTEENTH KNIGHT MODE\" UNLOCKED.\n')
                boss_rush_mode=1
                b=0
                time.sleep(2.5)
                clearScreen()
                mainMenu()
            else:
                sprint('CODE REJECTED. INSERT VALID CODE.\n')
                clearScreen()
                if boss_rush_mode==0:
                    title_menu_sel=4
                elif boss_rush_mode==1:
                    title_menu_sel=3
                b=0
        elif bonus=='disable codes':
            b=1
            title_menu_sel=0
            if boss_rush_mode==0:
                sprint('NO CODES TO DISABLE. HAVE A NICE DAY.\n')
                b=0
                clearScreen()
                mainMenu()
            else:
                sprint('DISABLING ALL CODES...\n')
                time.sleep(1.2)
                boss_rush_mode=0
                b=0
                clearScreen()
                mainMenu()
        else:
            b=0
            title_menu_sel=4
            sprint('Err: UnknownOption. Re-Attempt.\n')
            clearScreen()
    else:
        b=0
        title_menu_sel=0
        sprint('Invalid Value. Choose a listed option please.\n')
        mainMenu()
