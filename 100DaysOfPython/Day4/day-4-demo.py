#Rock Paper Scissors
import random

print('Welcome to the game of rock paper scissors')

choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")
if choice == 0:
    print('You chose Rock!')
if choice == 1:
    print('You chose Paper!')
if choice == 2:
    print('You chose Scissors!')

computer = random.randint(0,2)
# if (computer == 0):
#     computer_choice = 'Rock'
# elif (computer == 1):
#     computer_choice = 'Paper'
# else:
#     computer_choice = 'Scissors'

# print("The computer chose", computer_choice)

if (choice == 0 and computer == 1):
    print('You lose! The Computer won with Paper')
elif (choice == 1 and computer == 2):
    print('You lose! The Computer won with Scissors')
elif (choice == 2 and computer == 0):
    print('You lose! The Computer won with Rock')
elif (computer == choice):
    print('It is a tie! Try Again! ')
#else:
#    print('You win!')
#    print('Thanks for playing!')
#    break   
