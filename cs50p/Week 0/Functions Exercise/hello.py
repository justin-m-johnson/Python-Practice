def hello(to="world"):
    print("Hello, ", to)

name = input("What is your name? ")
hello(name)
hello()
##### Line 1 - hello(to) is "def"ined as a function. "to" is the variable that is passed within the function.
##### Line 5 - hello(name) - "name" is passed to the function in line 1, and converted to "to" variable, and printed out.
##### Line 1 - hello(to="world") - "world" in this case is the "Default" value here, in case no value is passed to it.