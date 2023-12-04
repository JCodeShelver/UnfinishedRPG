b=0
c=0
DevMode=0
thirteenKnightMode=0
ModernMode=0
def sprint(str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)
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
            sprint ('\n############################\n\n')
            start()
    elif DevMode==1 and thirteenKnightMode==0:
        sprint('-----The Twelfth Knight-----\n1) New Game\n2) Load Game\n3) Settings\n4) Bonus Content\n5) DEVTOOLS\n----------------------------\n')
        Selection = input('> ')
        try:
            a=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            sprint ('\n############################\n\n')
            start()
    else:
        sprint('-----The Twelfth Knight-----\n1) New Game\n2) Load Game\n3) Settings\n4) Bonus Content\n----------------------------\n')
        Selection = input('> ')
        try:
            a=int(Selection)
        except ValueError:
            sprint('Err: UnknownSelection. Try the number of the option requested.\n')
            time.sleep(1)
            sprint ('\n############################\n\n')
            start()
def UNDEV():
        sprint('ARE YOU SURE YOU WANT TO EXIT DEVELOPER MODE? Y/')
        undev=input('N ').lower()
        if undev=='y':
            sprint('THANK YOU FOR USING DEVELOPER MODE.\n')
            time.sleep(.2)
            sprint ('\n############################\n\n')
            DevMode=0
            start()
        elif undev=='n':
            sprint('DEVELOPER MODE WILL STAY ACTIVE.\n')
from SaveLoad import *
import sys
import time
from Battle import *
from Chest import *
from EnemyList import *
from LevelUp import *
while c==0:
    c=1
    start()
while b==0:
    if a==1 and thirteenKnightMode==0 and ModernMode==0:
        b=1
        a=0
        from DefaultHero import *
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
        from DefaultHero import *
        sprint('Enter the chosen one\'s name')
        name=input(': ')
        hero['name'] = name
        sprint('Choose your primary talent: |Medic|Cybersoldier|Scientist|Hacker')
        role=input('| ').lower()
        hero['role'] = role
        if role=='hacker':
            sprint('You have become a hacker!\nYou can hack advanced electronics!\nHacking abilities increased from minimal to veteran!\n')
            player['stats']['hacking'] = 1
        elif role=='medic':
            sprint('You have become a medic!\nYou medical abilities are growing!\nAs you help more \
people, you get more skills!\nYou can now do advanced medical procedures!\n')
            player['stats']['medical'] = 1
        elif role=='cybersoldier':
            sprint('You have become a cybersoldier!\nYou attacking capabilities are growing!\nAs your digital implant enhances \
your body, you get more agile and tactical!\nYou can now use advanced military grade cybertechnology without hacking or alarms!\n')
            player['stats']['cybergadgets'] = 1
        elif role=='scientist':
            sprint('You have become a scientist!\nYou chemical abilities are growing!\nAs the knowledge floods \
your mind, you get smarter!\nYou can now make serums!\n')
            player['stats']['serums'] = 1
        else:
            b=0
            a=1
    elif a==1 and thirteenKnightMode==1:
        b=1
        a=0
        from AlternateDefaultHero import *
        from AlternateEnemyList import *
        from AlternateTournament import *
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
                pass
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
            sprint ('\n############################\n\n')
            start()
    elif (a==3 and thirteenKnightMode==0) or (a==2 and thirteenKnightMode==1):
        a=0
        b=1
        sprint('Choose what setting to change: |Back|Dialogue Speed|Difficulty')
        settingedit=input('| ').lower()
        if settingedit=='dialogue speed':
            sprint('What speed should dialogue be spoken?\nSlowest is 1, Fastest is 3')
            sps=input('. ').strip()
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
                sprint ('\n############################\n\n')
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
                sprint ('\n############################\n\n')
                start()
            except ValueError:
                a=3
                b=0
                sprint('Err: UnknownDifficultySetting. Attempt again.\n')
                sprint ('\n############################\n\n')
        elif settingedit=='back':
            a=0
            b=0
            sprint('\n############################\n\n')
            start()
        else:
            a=3
            b=0
            sprint('Err: UnknownOption. Attempt again.\n')
            sprint ('\n############################\n\n')
    elif (a==4 and thirteenKnightMode==0) or (a==3 and thirteenKnightMode==1):
        sprint('|Buy DLC|Enter Code|Disable Codes')
        bonus=input('| ').lower()
        if bonus=='buy dlc':
            b=1
            a=0
            sprint('No DLC available yet. :(\n')
            b=0
            sprint ('\n############################\n\n')
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
                    sprint('\n############################\n\n')
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
                        sprint('\n############################\n\n')
                        start()
            elif diff=='ThirteenthKnight':
                if DevMode==0:
                    sprint('CODE INSERTED SUCCESSFULLY. \"THIRTEENTH KNIGHT MODE\" UNLOCKED.\n')
                    thirteenKnightMode=1
                    b=0
                    sprint('\n############################\n\n')
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
                        sprint('\n############################\n\n')
                        start()
            elif diff=='ModernMode':
                sprint('CODE INSERTED SUCCESSFULLY. A modernized version has appeared when starting a new game\n')
                ModernMode=1
                b=0
                sprint('\n############################\n\n')
                start()
            else:
                sprint('CODE REJECTED. INSERT VALID CODE.\n')
                sprint('\n############################\n\n')
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
                sprint('\n############################\n\n')
                start()
            elif ModernMode==1 or DevMode==1 or thirteenKnightMode==1:
                sprint('DISABLING ALL CODES...\n')
                time.sleep(1.2)
                ModernMode=0
                DevMode=0
                thirteenKnightMode=0
                b=0
                sprint('\n############################\n\n')
                start()
        else:
            b=0
            a=4
            sprint('Err: UnknownOption. Re-Attempt.\n')
            sprint('\n############################\n\n')
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
\n\n    DEBUG-\n        A DEBUG MODE USING THE PDB MODULE.\n    EXITS INTO THE TERMINAL. NOT RECOMMENDED FOR AMATEURS.\n')
            sprint('\n############################\n\n')
            a=5
            b=0
        else:
            sprint('ERR: UNKNOWNOPTION. ATTEMPT AGAIN.\n')
            sprint('\n############################\n\n')
            a=5
            b=0
    else:
        b=0
        a=0
        sprint('Invalid Value. Choose a listed option please.\n')
        start()
