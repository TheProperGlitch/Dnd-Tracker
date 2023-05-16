import os
import json
#Editting a creature:
def c_edit():
    if f"{username}.json" in files:
        with open(f"{username}.json", "r") as file:
            user_objects = json.load(file)
        if user_objects["creature_amount"] == 0:
            print("Sorry, but it seems that you have no creatures to look at.")
        else:
            print("What creature would you like to edit?")
            creature_amount = user_objects["creature_amount"]
            creature_list = user_objects["creature_list"]
            for i in range(creature_amount):
                print(f"{i+1}: Name:{creature_list[str(i+1)][0]}, Health:{creature_list[str(i+1)][1]}, Dex Modifier:{creature_list[str(i+1)][2]} \n Notes:{creature_list[str(i+1)][3]}")
            editing = int(input(""))
            print("What would you like to edit (Name for name, Health for health, and so on.)?")
            print(f"Name: {creature_list[str(editing)][0]}")
            print(f"Health: {creature_list[str(editing)][1]}")
            print(f"Dexterity: {creature_list[str(editing)][2]}")
            print(f"Notes: {creature_list[str(editing)][3]}")
            stat = input("")
            if stat.lower() == "name":
                print("What would you like to make the name?")
                creature_list[str(editing)][0] = input("")
            if stat.lower() == "health":
                print("What would you like to make the health? (Must be made of number symbols.)")
                creature_list[str(editing)][1] = int(input(""))
            if stat.lower() == "dexterity":
                print("What would you like to make the dexterity? (Must be made of number symbols.)")
                creature_list[str(editing)][2] = int(input(""))
            if stat.lower() == "notes":
                print("What would you like to make the health? (Must be made of number symbols.)")
                creature_list[str(editing)][3] = input("")
            user_objects["creature_list"] = creature_list
            with open(f"{username}.json", "w") as file:
                json.dump(user_objects, file)
            print("Done!")
            

    else:
        print("Sorry, but it seems that you have no creatures to look at.")
#Making a new creature:
def c_make():
    creature = []
    creature_list = {}
    print("What would you like to name the creature? (The name must be lowercase and have no spaces.) \n(Example: bobby)")
    creature.append(input(""))
    print("How many points of health would you like to give this creature? \n(The health must be a full integer made with number symbols) \n(Example: 592)")
    creature.append(int(input(""))) 
    print("What is this creature's dexterity modifier. (The dexterity must be a full integer made with number symbols) \n(Example: 17)")
    creature.append(int(input("")))
    print("Is there any notes you would like to add? (Write plain text or leave empty) \n(Example: Will fly in 5 turns. Attacks in one turn.)")
    creature.append(input(""))
    if f"{username}.json" in files:
        with open(username+".json", "r") as file:
            user_objects = json.load(file)
        creature_amount = user_objects["creature_amount"]
        creature_amount += 1
        creature_list = user_objects["creature_list"]
        creature_list[creature_amount] = creature
        user_objects["creature_list"] = creature_list
        user_objects["creature_amount"] = creature_amount
        with open(f"{username}.json", "w") as file:
            json.dump(user_objects, file)
    else:
        creature_list = {1: creature}
        user_objects = {"creature_amount" : 1, "creature_list" : creature_list, "encounter_amount" : 0, "encounter_list" : {}}
        with open(f"{username}.json", "w") as file:
            json.dump(user_objects, file)
    print("Done!")
#Copying a creature that has already been made
def c_copy():
    if f"{username}.json" in files:
        with open(f"{username}.json", "r") as file:
            user_objects = json.load(file)
        if user_objects["creature_amount"] == 0:
            print("Sorry, but it seems that you have no creatures to copy.")
        else:
            print("What creature would you like to copy?")
            creature_amount = user_objects["creature_amount"]
            creature_list = user_objects["creature_list"]
            for i in range(creature_amount):
                print(f"{i+1}: Name:{creature_list[str(i+1)][0]}, Health:{creature_list[str(i+1)][1]}, Dex Modifier:{creature_list[str(i+1)][2]} \n Notes:{creature_list[str(i+1)][3]}")
            copying = int(input(""))
            creature = creature_list[str(copying)]
            creature_amount+=1
            creature_list[creature_amount] = creature
            user_objects["creature_amount"] = creature_amount
            user_objects["creature_list"] = creature_list
            with open(f"{username}.json", "w") as file:
                json.dump(user_objects, file)
            print("Done!")


    else:
        print("Sorry, but it seems that you have no creatures to copy.")
#Making an encounter
def e_make():
    print("Would you like to quick-make an encounter or be more detailed? (Q for quick make, D for detailed.) \nNote: Quick made encounters will not be saved.")
    encounter_type = input("")
    if encounter_type.lower() == "q":
        print("How many creatures are there?")
        amount_of_creatures=int(input(""))
        turn = 0
        initiative_tracking = {}
        while turn < amount_of_creatures:
            print("What is the creatures name?")
            name = input('')
            print("What is the creatures initiative? (Numbers only!)")
            initiative = int(input(''))
            while initiative in initiative_tracking:
                print("I'm sorry, but two creatures cannot have the same initiative.\nWhat should the new initiative be?")
                initiative = int(input(''))
            print("What is the creatures health? (Numbers only!)")
            health = input('')
            print("What other notes do you have?")
            notes = input('')
            creature = [name, initiative, health, notes]
            if health == "":
                health = 1
            initiative_tracking[initiative] = [creature]
            turn += 1
        playing = True
        while playing:
            for key in sorted (initiative_tracking.keys(), reverse=True):
                print(f"It is {initiative_tracking[key][0][0]}'s turn! \nWhat would you like to do? \nCommands:(H: Heal Self, D: Damage, A: Attack, N: Next, E: End)")
                action = input("")
                if action.lower() == "h":
                    print(f"{initiative_tracking[key][0][0]} is at {initiative_tracking[key][0][2]} health.")
                    print("For how much would you like heal for? (Integers only!)")
                    health_healed = int(input(""))
                    initiative_tracking[key][0][2] = str(health_healed + int(initiative_tracking[key][0][2]))
                    print(f"{initiative_tracking[key][0][0]} is now at {initiative_tracking[key][0][2]} health.")
                elif action.lower() == "d":
                    print(f"{initiative_tracking[key][0][0]} is at {initiative_tracking[key][0][2]} health.")
                    print("For how much damage would you like to do? (Integers only!)")
                    damage_dealt = int(input(""))
                    initiative_tracking[key][0][2] = str(int(initiative_tracking[key][0][2]) - damage_dealt)
                    print(f"{initiative_tracking[key][0][0]} is now at {initiative_tracking[key][0][2]} health.")
                elif action.lower() == "a":
                    print("")
                elif action.lower() == ("e"):
                    playing = False
                    break
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
os.chdir("People")
files = os.listdir('.')
files.remove("null..txt")
username = "Username####"
user_objects = {}
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