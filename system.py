import os

def c_edit():
    print("")

def c_make():
    creature = {}
    print("What would you like to name the creature? (The name must be lowercase and have no spaces.) \n(Example: bobby)")
    creature["name"] = input("")
    print("How many points of health would you like to give this creature? \n(The health must be a full integer made with number symbols) \n(Example: 592)")
    creature["health"] = int(input(""))
    print("What is this creature's order in the initative. (The initative must be a full integer made with number symbols) \n(Example: 17)")
    creature["initative"] = int(input(""))
    print("Is there any notes you would like to add? (Write plain text or leave empty) \n(Example: Will fly in 5 turns. Attacks in one turn.)")
    creature["notes"] = input("")
    print("Would you like to pre-make actions. (Y for yes, N for no)")
    choice3 = input("")
    if choice3.lower() == "y":
        print("")
def c_copy():
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
    print("Next choose between editing an existing creature, copying one that is made, or making a new one.\n(E for Edit, C for Copy, N for New)")
    choice2 = input("")
    if choice2.lower() == "e":
        c_edit()
    elif choice2.lower() == "n":
        c_make()
    elif choice2.lower() == "c":
        c_copy()
    else:
        print("I'm sorry, but it seems there was an error. Please restart the program.")
elif choice1.lower() == "e":
    print("Next choose between making, copying, editing, or using an encounter.\n(Type M, C, E, or U)")
    choice2 = input("")
    if choice2.lower() == "m":
        e_make()
    elif choice2.lower() == "c":
        e_copy()
    elif choice2.lower() == "e":
        e_edit()
    elif choice2.lower() == "u":
        e_use()
    else:
        print("I'm sorry, but it seems there was an error. Please restart the program.")
else:
    print("I'm sorry, but it seems there was an error. Please restart the program.")