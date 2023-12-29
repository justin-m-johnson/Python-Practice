def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            return int(input(prompt)) #tighten code up
        except ValueError:
            pass #This is a passive way of dealing with error
            #print("x is not an integer")
            #print("Use an Integer")
    
    #   else:
    #       break

main()






'''try:
    print(f"x is {x}")
except NameError:
    print("You have a NameError")
'''