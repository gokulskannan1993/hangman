from resources import stages, WORDS, won, lost


import random

game_over = False
lives = 6



# Generate a random word
answer = random.choice(WORDS).upper()
print(answer)


# Create blank array
display = []
for letter in answer:
    display += "_"



# For running in loop
while not game_over:

    print(stages[lives])


    # Ask for user input
    guess = input("Guess a letter: ").upper()

    


    # Checks for the match
    for position in range(0, len(answer)):
        letter = answer[position]
        if(guess == letter):
            display[position] = letter
    
    
    # Check for wrong guess
    if guess not in answer:
        lives -= 1
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(lost)

    # Print the display each time
    print(f"{' '.join(display)}")

    # If the player wins
    if "_" not in display:
        game_over = True
        print(won)
    


