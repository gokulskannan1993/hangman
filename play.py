from resources import stages, WORDS


import random

game_over = False



# Generate a random word
answer = random.choice(WORDS).upper()
print(answer)


# Create blank array
display = []
for letter in answer:
    display += "_"




while not game_over:
    # Ask for user input
    guess = input("Guess a letter: ").upper()





    for position in range(0, len(answer)):
        letter = answer[position]
        print(f"Current position is {letter} and guess is {guess}")
        if(guess == letter):
            display[position] = letter


    print(display)
    if "_" not in display:
        game_over = True
        print("Your win")


