import random
import statistics
import sys

print("Random number:")
number = random.randint(1, 10)
print(number)

print("\n" + "Shuffle cards:" )
cards = ["Jack", "Queen", "King"]
random.shuffle(cards)
for card in cards:
    print(card)

print("\n" + "This is a mean of 100 and 90")
print(statistics.mean([100, 90])) #function "mean" in module of "statistics"

print("Hello, my name is", sys.argv[1]) #based on this we need to run "python generate.py *NAME*"
