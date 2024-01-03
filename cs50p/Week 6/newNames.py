names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip()) #rstrip is the same as end=""

for name in sorted(names):
    print(f"hello, {name}")