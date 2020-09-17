room = "11"
direction = ""
while room != "31":
    if room == "11":
        direction = input("You can travel: (N)orth. ")
        if direction.lower() == "n":
            print("Direction: " + direction)
            room = "12"
        else:
            print("Not a valid direction!")
    elif room == "12":
        direction = input("You can travel: (N)orth or (E)ast or (S)outh. ")
        if direction.lower() == "n":
            print("Direction: " + direction)
            room = "13"
        elif direction.lower() == "e":
            print("Direction: " + direction)
            room = "22"
        elif direction.lower() == "s":
            print("Direction: " + direction)
            room = "11"
        else:
            print("Not a valid direction!")
    elif room == "13":
        direction = input("You can travel: (E)ast or (S)outh. ")
        if direction.lower() == "e":
            print("Direction: " + direction)
            room = "13"
        elif direction.lower() == "s":
            print("Direction: " + direction)
            room = "11"
        else:
            print("Not a valid direction!")
    elif room == "21":
        direction = input("You can travel: (N)orth. ")
        if direction.lower() == "n":
            print("Direction: " + direction)
            room = "22"
        else:
            print("Not a valid direction!")
    elif room == "22":
        direction = input("You can travel: (S)outh or (W)est. ")
        if direction.lower() == "s":
            print("Direction: " + direction)
            room = "21"
        elif direction.lower() == "w":
            print("Direction " + direction)
            room = "12"
        else:
            print("Not a valid direction!")
