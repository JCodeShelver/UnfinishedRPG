import os
import sys
import time
import pickle

from DefaultHero import player


def save():
    if not os.path.isfile('do-not-touch.dat'):
        with open('do-not-touch.dat', 'wb') as f:
            pickle.dump(player, f)
            print ("\nGame has been saved!\n")
    elif not os.path.isfile('do-not-touch(1).dat'):
        with open('do-not-touch(1).dat', 'wb') as f:
            pickle.dump(player, f)
            print ("\nGame has been saved!\n")
    elif not os.path.isfile('do-not-touch(2).dat'):
        with open('do-not-touch(2).dat', 'wb') as f:
            pickle.dump(player, f)
            print ("\nGame has been saved!\n")
    elif not os.path.isfile('do-not-touch(3).dat'):
        with open('do-not-touch(3).dat', 'wb') as f:
            pickle.dump(player, f)
            print ("\nGame has been saved!\n")
    else:
        print("\nAll files have been taken!")

def load():
    save = input('What save file would you like to load?\n1\n2\n3\n4\n> ')
    try:
        if save == "1" and os.path.isfile('do-not-touch.dat'):
            with open('do-not-touch.dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "2" and os.path.isfile('do-not-touch(1).dat'):
            with open('do-not-touch(1).dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "3" and os.path.isfile('do-not-touch(2).dat'):
            with open('do-not-touch(2).dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        elif save == "4" and os.path.isfile('do-not-touch(3).dat'):
            with open('do-not-touch(3).dat', 'rb') as f:
                player = pickle.load(f)
                print ("\nGame has been loaded!\n")
        else:
            print("\nInvalid save file!")
            load()
    except FileNotFoundError:
        print('Save file not located! Try to load a different file.')
        load()


