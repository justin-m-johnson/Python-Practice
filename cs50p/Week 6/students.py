with open("students.csv") as file:
    for line in file:
        row = line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")

'''you can also split the variables instead of assigning them to the same in a list'''

print("This is splitting in each value of 'Name' and 'House'")
with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
        print(f"{name} is in {house}")