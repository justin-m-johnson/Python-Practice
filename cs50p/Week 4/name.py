import sys

#argv = Argument Vector (sys.argv)
'''
try:
    print("Hello my name is", sys.argv[1])
except IndexError:
    print("Too few arguments...")

# in this command, if we don't enter anything after "name.py" to fill in sys.argv[1] it will have an Index Error. We need to catch it
'''

# Check for Errors
if len(sys.argv) < 2:
    sys.exit("Too Few Arguments.")


#this will print all of list (including 0)
#for arg in sys.argv:
#    print("Hello, my name is", arg)

#Lets Slice it
for arg in sys.argv[1:]:
    print("Hello, my name is", arg)