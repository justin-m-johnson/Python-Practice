name = input("Whats your name? ")

'''
if name == "Harry" or name == "Hermoine" or name == "Ron":
    print("Gryffindore")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''
#Lets fix the code above with a Match

match name:
    case "Harry" | "Hermoine" | "Ron":
        print("Gryffindore")
    case "Draco":
        print("Slytherin")
    case _:
        print("Who?")