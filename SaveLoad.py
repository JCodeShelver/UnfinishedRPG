import os
import sys
import time
import pickle
from DefaultHero import *

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
        if save == "1" and os.path.isfile('do-not-touch.dat') == True:
            with open('do-not-touch.dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "2" and os.path.isfile('do-not-touch(1).dat') == True:
            with open('do-not-touch(1).dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "3" and os.path.isfile('do-not-touch(2).dat') == True:
            with open('do-not-touch(2).dat', 'rb') as f:
                player = pickle.dump(f)
                print ("\nGame has been loaded!\n")
        elif save == "4" and os.path.isfile('do-not-touch(3).dat') == True:
            with open('do-not-touch(3).dat', 'rb') as f:
                player = pickle.dump(f)
                print ("\nGame has been loaded!\n")
    except FileNotFoundError:
        print('Save file not located! Try to load a different file.')


