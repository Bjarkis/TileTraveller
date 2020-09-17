room = "11"
direction = ""
while room != "31":
    if room == "11":
        print("You can travel: (N)orth.")
        direction = input("Direction: ")
        if direction.lower() == "n":
            room = "12"
        else:
            print("Not a valid direction!")
    elif room == "12":
        print("You can travel: (N)orth or (E)ast or (S)outh. ")
        direction = input("Direction: ")
        if direction.lower() == "n":
            room = "13"
        elif direction.lower() == "e":
            room = "22"
        elif direction.lower() == "s":
            room = "11"
        else:
            print("Not a valid direction!")
    elif room == "13":
        print("You can travel: (E)ast or (S)outh. ")
        direction = input("Direction: ")
        if direction.lower() == "e":
            room = "23"
        elif direction.lower() == "s":
            room = "11"
        else:
            print("Not a valid direction!")
    elif room == "21":
        print("You can travel: (N)orth. ")
        direction = input("Direction: ")
        if direction.lower() == "n":
            room = "22"
        else:
            print("Not a valid direction!")
    elif room == "22":
        print("You can travel: (S)outh or (W)est. ")
        direction = input("Direction: ")
        if direction.lower() == "s":
            room = "21"
        elif direction.lower() == "w":
            room = "12"
        else:
            print("Not a valid direction!")
    elif room == "23":
        print("You can travel: (E)ast or (W)est. ")
        direction = input("Direction: ")
        if direction.lower() == "e":
            room = "33"
        elif direction.lower() == "w":
            room = "13"
        else:
            print("Not a valid direction!")
    elif room == "33":
        print("You can travel: (W)est or (S)outh ")
        direction = input("Direction: ")
        if direction.lower() == "w":
            room = "23"
        elif direction.lower() == "s":
            room = "32"
        else:
            print("Not a valid direction!")
    elif room == "32":
        print("You can travel: (N)orth or (S)outh ")
        direction = input("Direction: ")
        if direction.lower() == "n":
            room = "33"
        elif direction.lower() == "s":
            room = "31"
        else:
            print("Not a valid direction!")
            
print("Victory!")