x = int(input("What is x? "))
y = int(input("What is y? "))

'''
Below are IF statements, it will continue to run to the end, answering only if its true, not when false, such that:
if x is 2
and y is 1
The output will be:
x is greater than y
x is great than or equal to y
x doesn't equal y
'''
print("Start If Statements")
if x < y:
    print("x is less than y")

if x > y:
    print("x is greater than y")

if x == y:
    print("x equals y")

if x <= y:
    print("x is less than or equal to y")

if x >= y:
    print("x is greater than or equal to y")

if x != y:
    print("x doesn't equal y")





'''
Below are elif statements, these will stop the code once we hit a True statement
'''

print("Start ElIf Statements")
print("These are elif statements, these will stop the code once we hit a True statement")

if x < y:
    print("x is less than y")

elif x > y:
    print("x is greater than y")

elif x == y:
    print("x equals y")

# OR you don't really need the above because the third elif "x == y" is given. You can just use:
#############################
# else:
#    print("x is equal to y")
#############################
    
'''
OR Statements
'''
print("Start OR statements")
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")

print("Much simpler OR Statement")
if x != y:
    print("x is not equal to y")
else:
    print("x is equal to y")
    