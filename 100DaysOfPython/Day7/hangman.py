import random

word_list = ["banana", "apple", "pear"]

# TODO - 1 Choose Random Word
word = random.choice(word_list)
print(word)


# TODO - 2 Generate blanks for word
blanks = "_" * len(word)
print(blanks)


# TODO - 3 Ask user to guess word
display = blanks
guess = ""
tries = 0
game_over = False
correct_letters = []

# TODO - 4 Check if user guessed correctly
while guess != word and tries < 11 and game_over == False:
    if tries == 10:
        print("You lose! The word was " + word)
        game_over = True
    else:
        guess = input("Guess a letter: ").lower()
        if guess in word:
            for i, letter in enumerate(word):
                if letter == guess:
                    display = display[:i] + guess + display[i+1:]
            if "_" not in display:
                game_over = True
                print("You win!")
        else:
            tries += 1
        print(display)

        if "_" not in display:
            game_over = True
            print("You win!")
        tries += 1