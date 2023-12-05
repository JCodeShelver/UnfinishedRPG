import sys
import time

_delay = 0.04

def sprint(str: str):
    for letter in str:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(_delay)

def setSprintSpeed(spd: float):
    _delay = spd

def clearScreen():
    if 'idlelib.run' in sys.modules:
        sprint('\n############################\n\n')
    else:
        import os
        os.system('cls' if os.name == 'nt' else 'clear')