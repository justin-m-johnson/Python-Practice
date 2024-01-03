students = []

with open("students.csv") as file:
    for line in file:
        name, house = line.rstrip().split(",")
#        student = {} #this creates a dictionary
#        student["name"] = name
#        student["house"] = house
# One liner:
        student = {"name" : name, "house" : house}
        students.append(student)

def get_name(student):
    return student["name"]

def get_house(student):
    return student["house"]

print("the following is sorted by name")

for student in sorted(students, key=get_name):
    print(f"{student['name']} is in {student['house']}")

print("\n" + "the following is sorted by name - Reversed")

for student in sorted(students, key=get_name, reverse=True):
    print(f"{student['name']} is in {student['house']}")


print("\n" + "The following is sorted by house")

for student in sorted(students, key=get_house):
    print(f"{student['name']} is in {student['house']}")

print("\n" + "The following is sorted by house - reverse")

for student in sorted(students, key=get_house, reverse=True):
    print(f"{student['name']} is in {student['house']}")

