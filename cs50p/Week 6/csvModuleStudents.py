import csv
#this module deals with all the problems and corner cases for us - such as addresses with commas in them in a CSV!

students = []

with open("students.csv") as file:
    reader = csv.DictReader(file) 
    for row in reader:
        students.append({"name": row["name"], "home": row["home"]})

#check newStudents.py - The key=lambda replaced the get_name(student) function we created!!!
# Lambda is an anonymous function
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")