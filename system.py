import os
import json
import random
#Showing all creatures:
def c_show():
    if f"{username}.json" in files:
        with open(f"{username}.json", "r") as file:
            user_objects = json.load(file)
        if user_objects["creature_amount"] == 0:
            print("Sorry, but it seems that you have no creatures to look at.")
        else:
            creature_amount = user_objects["creature_amount"]
            creature_list = user_objects["creature_list"]
            for i in range(creature_amount):
                print(f"{i+1}: Name:{creature_list[str(i+1)][0]}, Health:{creature_list[str(i+1)][1]}, Dex Modifier:{creature_list[str(i+1)][2]} \n Notes:{creature_list[str(i+1)][3]}")

#Editting a creature:
def c_edit():
    """
    Allows the user to edit a creature's attributes.

    This function checks if the user has any creatures, prompts them to select a creature,
    and then allows them to edit the creature's name, health, dexterity, or notes.
    The edited information is then saved to a JSON file.

    Raises:
        FileNotFoundError: If the user does not have any creatures to edit.

    Returns:
        None
    """
    # Function code goes here
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
    """
    Prompts the user to create a new creature and saves it to a JSON file.

    This function guides the user to enter the name, health, dexterity, and notes of a new creature.
    It then checks if the user already has a JSON file. If the file exists, it adds the new creature
    to the existing creature list. If the file does not exist, it creates a new JSON file with the
    creature as the first entry.

    Returns:
        None
    """
    # Function code goes here
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
    """
    Allows the user to create an encounter.

    This function provides the user with options to quickly make an encounter or create a detailed encounter.
    If the user selects a quick make, they can specify the number of creatures and their attributes interactively.
    If the user selects a detailed encounter, they can choose creatures from an existing list stored in a JSON file.

    Returns:
        None
    """
    # Function code goes here
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
                if playing == False:
                    break
                active = True
                while active:
                    print(f"It is {initiative_tracking[key][0][0]}'s turn! \nWhat would you like to do? \nCommands:(H: Heal Self, D: Damage, N: Next, E: End)")
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
                    elif action.lower() == "n": 
                        active = False
                    elif action.lower() == "e":
                        playing = False
                        active = False
    else:
        if f"{username}.json" in files:
            with open(f"{username}.json", "r") as file:
                user_objects = json.load(file)
            creature_list = user_objects["creature_list"]
            creature_amount = user_objects["creature_amount"]
            encounter_list = user_objects["encounter_list"]
            encounter_amount = user_objects["encounter_amount"]
            non_added_list = creature_list.copy()
            encounter = []
            while True:
                print(f"Creatures added: {encounter}")
                print("Which creature would you like to add to the encounter? Integer only!")
                print("0: End")
                for creature_key in non_added_list:
                    creature = non_added_list[creature_key]
                    print(f"{creature_key}: Name: {creature[0]}, Health: {creature[1]}, Initiative: {creature[2]}, Notes: {creature[3]}")
                chosen = int(input())
                if chosen == 0:
                    print("Done")
                    break
                encounter.append(non_added_list[str(chosen)]) 
                non_added_list.pop(str(chosen))
                if len(non_added_list) == 0:
                    print("All creatures added!")
                    break
            encounter_amount += 1
            encounter_list[encounter_amount] = encounter
            user_objects["encounter_amount"] = encounter_amount
            user_objects["encounter_list"] = encounter_list
            with open(f"{username}.json", "w") as file:
                json.dump(user_objects, file)
        else:
            print("Sorry, but it seems you have no creatures, please make some and then try again.")

#Copying an encounter that has already been made
def e_copy():  
    print("")
#Editing an encounter that has already been made
def e_edit():
    print("")
#Using a made encounter
def e_use():
    if f"{username}.json" in files:
        with open(f"{username}.json", "r") as file:
            user_objects = json.load(file)
        encounter_list = user_objects["encounter_list"]
        encounter_amount = user_objects["encounter_amount"]
        if encounter_amount == 0:
            print("Sorry, but we could not find any encounters in your file. \nTry making an encounter.")
        else:
            print("Which encounter would you like to use:")
            for object in encounter_list:
                print(f"{str(object)}: {encounter_list[object]}")
            encounter_choice = input("")
            encounter = encounter_list[encounter_choice]
            initiative_tracking = {}
            for creature in encounter:
                name = creature[0]
                initiative = random.randint(1,20) + creature[1]
                while initiative in initiative_tracking:
                    initiative = random.randint(1,20) + creature[1]
                health = creature[2]
                notes = creature[3]
                initiative_tracking[initiative] = [creature]

            playing = True
            while playing:
                for key in sorted(initiative_tracking.keys(), reverse=True):
                    if playing == False:
                        break
                    active = True
                    while active:
                        print(f"It is {initiative_tracking[key][0][0]}'s turn! \nWhat would you like to do? \nCommands:(H: Heal Self, D: Damage, N: Next, E: End)")
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
                        elif action.lower() == "n":
                            active = False
                        elif action.lower() == "e":
                            playing = False
                            active = False
    else:
        print("Sorry, but we could not find a file with your name. \nTry making a creature.")


#Start of code:try:
#Start of code:
try:
    os.chdir("Users")
except FileNotFoundError:
    print("DIRECTORY NOT FOUND")
    os.mkdir("Users")
    os.chdir("Users")
files = os.listdir('.')
#This is here to remove the file added to github by the repo
try:
    files.remove("null..txt")
except ValueError:
    print("FILE NOT FOUND. SKIPPING...")
username = "Username####"
user_objects = {}
# ---Grab the discord user's ID and save it to the variable "username"---
print("Hello and welcome to the AV D&D Tracker. Start off by picking between managing creatures/characters or encounters. \n(C for Creatures, E for Encounters)")
choice1 = input("")
if choice1.lower() == "c":
    print("Next choose between editing an existing creature, copying one that is made, or making a new one.\n(S for Show, E for Edit, C for Copy, N for New)")
    choice2 = input("")
    if choice2.lower() == "s":
        c_show()
    if choice2.lower() == "e":
        c_edit()
    elif choice2.lower() == "n":
        c_make()
    elif choice2.lower() == "c":
        c_copy()
    else:
        print("I'm sorry, but it seems there was an error. Please restart the program.")
elif choice1.lower() == "e":
    print("Next choose between making or using an encounter.\n(Type M or U)")
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