import os

def c_edit():
    print("")

def c_make():
    print("")

def e_make():
    print("")

def e_copy():
    print("")

def e_edit():
    print("")

def e_use():
    print("")

print("Hello and welcome to the AV D&D Tracker. Start off by picking between managing creatures/characters or encounters. \n(C for Creatures, E for Encounters)")
choice1 = input("")
if choice1.lower() == "c":
    print("Next choose between editing an existing creature or making a new one.\n(E for Edit, N for New)")
    choice2 = input("")
    if choice2.lower == "e":
        c_edit()
    elif choice2.lower == "n":
        c_make()
    else:
        print("I'm sorry, but it seems there was an error. Please restart the program.")
elif choice1.lower() == "e":
    print("Next choose between making, copying, editing, or using an encounter.\n(Type M, C, E, or U)")
    choice2 = input("")
    if choice2.lower == "m":
        e_make()
    elif choice2.lower == "c":
        e_copy()
    elif choice2.lower == "e":
        e_edit()
    elif choice2.lower == "u":
        e_use()
    else:
        print("I'm sorry, but it seems there was an error. Please restart the program.")
else:
    print("I'm sorry, but it seems there was an error. Please restart the program.")