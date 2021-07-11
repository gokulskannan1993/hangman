from resources import stages, WORDS, won, lost, logo, clear


import random

game_over = False
lives = 6


# Display logo for the first time
clear()
print(logo)



# Generate a random word
answer = random.choice(WORDS).upper()


# Create blank array
display = []
for letter in answer:
    display += "_"

print(f"{' '.join(display)}")



# For running in loop
while not game_over:
    print(stages[lives])


    # Ask for user input
    guess = input("Guess a letter: ").upper()
    clear()
    print(logo)




    # if the guess is previously guessed
    if guess in display:
        print(f"You have already guessed the letter '{guess}'")

    


    # Checks for the match
    for position in range(0, len(answer)):
        letter = answer[position]
        if(guess == letter):
            display[position] = letter
    
    
    # Check for wrong guess
    if guess not in answer:
        lives -= 1
        print(f"\n\nYou guessed wrong! {guess} is not in the word. You lost a life.\n")
        if lives == 0:
            game_over = True
            print(stages[lives])
            print(f"The Answer was {answer}")
            print(lost)

    # Print the display each time
    print(f"{' '.join(display)}")

    # If the player wins
    if "_" not in display:
        game_over = True
        print(won)
    


