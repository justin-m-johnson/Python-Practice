#This is a documentation of different Exceptions and Errors
#This will not run.

#Syntax Error Example:
'''
print("Hello World)
'''

#The error above is a Syntax error, involves a user to intervene and complete the Syntax. In this case, close the quotations


########################################     
#Value Error
'''
x = int(input("what is x? "))
print(f"x is {x}")
'''
#In this case, if the user enters a STR instead of an INT , you create a "ValueError" (ValueError: invalid literal for int() with base10: 'str')
#To fix this: Write code with Error Handling in mind 
# "Program Defensively"
# Use "try" and "except" (see number.py)

