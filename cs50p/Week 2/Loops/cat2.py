#This is going to demonstrate For loops
'''
for i in [0, 1, 2]:
    print("meow")
'''
### This is better written as

for i in range(3):
    print("meow")

#Even Simpler
    
print("MeOw\n" * 3, end="")


#While Loop with MEOW!

while True: #This creates an "Infinite loop"
    n = int(input("What is n?: "))
    if n > 0:
        break 
    #this forces user to give an integer greater than 0

for i in range(n):
    print("MEOW!")