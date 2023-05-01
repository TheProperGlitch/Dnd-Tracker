import os
import json
os.chdir("People")
#Editting a creature:
def c_edit():
    print("")

#Making a new creature:
def c_make():
    creature = []
    creature_list = []
    print("What would you like to name the creature? (The name must be lowercase and have no spaces.) \n(Example: bobby)")
    creature.append(input(""))
    print("How many points of health would you like to give this creature? \n(The health must be a full integer made with number symbols) \n(Example: 592)")
    creature.append(int(input(""))) 
    print("What is this creature's order in the initative. (The initative must be a full integer made with number symbols) \n(Example: 17)")
    creature.append(int(input("")))
    print("Is there any notes you would like to add? (Write plain text or leave empty) \n(Example: Will fly in 5 turns. Attacks in one turn.)")
    creature.append(input(""))
    if f"{username}.txt" in files:
        with open(f"{username}.txt", "r") as file:
            data = file.read()
        print(data)
        exec(data)
        print(creature_list)
        creature_list.append(creature)
        with open(f"{username}.txt", "w") as file:
            file.write(f"creature_list = {creature_list}")
    else:
        print("path 2")
        with open(f"{username}.txt", "w") as file:
            file.write(f"creature_list = [{creature}]")
    print("Done!")
        
    

#Copying a creature that has already been made
def c_copy():
    print("")

#Making an encounter
def e_make():
    print("")
#Copying an encounter that has already been made
def e_copy():
    print("")
#Editing an encounter that has already been made
def e_edit():
    print("")

#Using a made encounter
def e_use():
    print("")

#Start of code:
files = os.listdir('People')
files.remove("null..txt")
username = "Username####"
# ---Grab the discord user's ID and save it to the variable "username"---
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