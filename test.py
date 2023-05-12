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
        print(f"It is {initiative_tracking[key][0][0]}'s turn! \nhat would you like to do?")
        action = input("")
        if action == "Heal":
            print("Heal")
        elif action == ("End"):
            playing = False
            break


