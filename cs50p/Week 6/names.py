'''
names = []

for _ in range(3):
    names.append(input("Whats your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
'''
name=input("Whats your name? ")
#open is a function to "open" a file, and "w" is going to allow it to write (but it overwrites), "a" allows to append , as well as create the file if one doesnt exist

'''Instead of the following code'''
#file = open("names.txt", "a")

''' use this code instead (with)'''
with open("names.txt", "a") as file:
    file.write(f"{name}\n") #Add new line to fix file issue 

    '''and remove the close()'''
#file.close()