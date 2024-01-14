import re  # This is the regex library

# re.search(pattern, search, flag=0)


email = input("What is your email?: ").strip()
"""
if "@" in email and "." in email:
    print("valid")
else:
    print("invalid")


username, domain = email.split("@")

if username and domain.endswith(".edu"):
    print("valid")
else:
    print("invalid")


##This is a lot of code - Regex saves the day
"""

if re.search("+.@.+['.'].", email):
    print("valid")
else:
    print("invalid")
