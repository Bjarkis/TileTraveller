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
