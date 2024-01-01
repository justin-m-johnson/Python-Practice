'''
names = []

for _ in range(3):
    names.append(input("Whats your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
'''
name=input("Whats your name? ")
#open is a function to "open" a file, and "w" is going to allow it to write (but it overwrites), "a" allows to append , as well as create the file if one doesnt exist
file = open("names.txt", "a")
file.write(f"{name}\n") #Add new line to fix file issue 
file.close()