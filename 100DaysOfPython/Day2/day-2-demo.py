print("Welcome to the tip calulator!")
print("What was the total bill?")
bill = input()
print("What percentage tip would you like to give? 10, 12, or 15?")
tip = input()
print("How many people to split the bill?")
people = input()

bill = float(bill)
tip = int(tip)
people = int(people)

total_tip = bill * tip / 100
total_bill = bill + total_tip